"""Transparent simulation, not a real LLM agent or a published-method reproduction."""
from dataclasses import dataclass, replace
from itertools import combinations
from typing import Optional, Tuple
import numpy as np

STAGES = ('intent', 'plan', 'retrieval', 'evidence', 'tool_result', 'state_update', 'pre_action')
FAULTS_BY_STAGE = (
    ('destination', 'permission'), ('quantity', 'permission'),
    ('sku', 'evidence'), ('evidence', 'sku'),
    ('stock', 'price'), ('quantity', 'destination'), ('permission', 'price'),
)
PROFILES = ('retrieval_heavy', 'execution_heavy')
STAGE_WEIGHTS = {
    'retrieval_heavy': (0.05, 0.08, 0.43, 0.25, 0.07, 0.06, 0.06),
    'execution_heavy': (0.05, 0.04, 0.07, 0.09, 0.35, 0.32, 0.08),
}
RULE_COST = 1.0
EVIDENCE_COST = 1.5

@dataclass(frozen=True)
class Case:
    case_id: str
    profile: str
    budget: int
    target_quantity: int
    faulty: bool
    fault_stage: int
    fault_type: str
    deadline: int
    repair_uniform: float
    route_uniform: float


def generate_cases(seed: int, count: int, prefix: str):
    rng = np.random.default_rng(seed)
    cases = []
    for j in range(count):
        profile = PROFILES[int(rng.integers(0, 2))]
        faulty = bool(rng.random() < 0.60)
        stage = int(rng.choice(7, p=STAGE_WEIGHTS[profile])) if faulty else -1
        ftype = str(rng.choice(FAULTS_BY_STAGE[stage])) if faulty else 'none'
        horizon = int(rng.choice(3, p=[0.15, 0.55, 0.30])) if faulty else 0
        deadline = min(6, stage + horizon) if faulty else -1
        cases.append(Case(f'{prefix}-{seed}-{j:05}', profile,
                          int(rng.integers(180, 501)), int(rng.integers(1, 4)),
                          faulty, stage, ftype, deadline, float(rng.random()),
                          float(rng.random())))
    return cases


def intended_state(case: Case):
    """Trusted initial data: all values satisfy a fixed user intent."""
    return {
        'sku': 'compatible_product',
        'price': case.budget - 40,
        'quantity': case.target_quantity,
        'destination': 'allowed_region',
        'permission': True,
        'proof': 'verified_source',
        'stock': case.target_quantity + 2,
    }


def inject_fault(state, case: Case):
    bad = dict(state)
    f = case.fault_type
    if f == 'sku':
        bad['sku'] = 'incompatible_product'
    elif f == 'price':
        bad['price'] = case.budget + 25
    elif f == 'quantity':
        bad['quantity'] = case.target_quantity + 1
    elif f == 'destination':
        bad['destination'] = 'disallowed_region'
    elif f == 'permission':
        bad['permission'] = False
    elif f == 'evidence':
        bad['proof'] = 'unsupported_claim'
    elif f == 'stock':
        bad['stock'] = 0
    else:
        raise ValueError(f)
    assert set(bad) == set(state), 'fault must preserve the schema'
    return bad


def rule_verifier(state, case: Case):
    """Check stated user constraints; deliberately cannot validate external evidence."""
    return (state['price'] <= case.budget and
            state['quantity'] == case.target_quantity and
            state['destination'] == 'allowed_region' and
            state['permission'] is True)


def evidence_verifier(state, case: Case):
    """Check trusted synthetic catalog/provenance fields, not local user constraints."""
    return (state['sku'] == 'compatible_product' and
            state['proof'] == 'verified_source' and
            state['stock'] >= case.target_quantity)


def verify(state, case, kind):
    if kind == 'rule':
        return rule_verifier(state, case)
    if kind == 'evidence':
        return evidence_verifier(state, case)
    if kind == 'heterogeneous':
        return rule_verifier(state, case) and evidence_verifier(state, case)
    raise ValueError(kind)


def checkpoint_cost(kind):
    return {'rule': RULE_COST, 'evidence': EVIDENCE_COST,
            'heterogeneous': RULE_COST + EVIDENCE_COST}[kind]


def simulate(case: Case, positions: Tuple[int, ...], kind='heterogeneous',
             route_flip_probability=0.0, alternate_positions: Optional[Tuple[int, ...]]=None):
    """One fault max; detection always correct, but repair succeeds with probability 0.9.

    Deadline denotes the last stage before a synthetic irreversible side effect.
    A missed deadline is scored as an unsafe terminal outcome; there is no real API.
    """
    if alternate_positions is not None and case.route_uniform < route_flip_probability:
        positions = alternate_positions
    assert all(0 <= i < 7 for i in positions)
    state = intended_state(case)
    faulty_active, detected, success, unsafe, abort = False, False, False, False, False
    checks, cost, detection_stage = 0, 0.0, -1
    for stage in range(7):
        if case.faulty and stage == case.fault_stage:
            state = inject_fault(state, case)
            faulty_active = True
        if stage in positions:
            checks += 1
            cost += checkpoint_cost(kind)
            if not verify(state, case, kind):
                detected = True
                detection_stage = stage
                if case.repair_uniform < 0.9:
                    # Verified rollback to the clean state; proceed normally.
                    state = intended_state(case)
                    faulty_active = False
                else:
                    # Safe abort: no unsafe side effect, but the goal is not completed.
                    abort = True
                    break
        if faulty_active and stage >= case.deadline:
            unsafe = True
            break
    if not unsafe and not abort:
        success = True
    assert sum((success, unsafe, abort)) == 1
    return {
        'case_id': case.case_id, 'profile': case.profile,
        'faulty': int(case.faulty), 'fault_stage': case.fault_stage,
        'fault_type': case.fault_type, 'deadline': case.deadline,
        'detected': int(detected), 'detected_at': detection_stage,
        'detection_lag': detection_stage-case.fault_stage if detected else -1,
        'success': int(success), 'unsafe': int(unsafe), 'safe_abort': int(abort),
        'checks': checks, 'verification_cost': cost,
    }


def optimize_positions(dev_cases, kind='heterogeneous', k=3):
    """Development-only exhaustive selection. Freeze before evaluating test cases."""
    candidates = list(combinations(range(7), k))
    outcomes = []
    for positions in candidates:
        rows = [simulate(c, positions, kind) for c in dev_cases]
        unsafe = sum(r['unsafe'] for r in rows)
        aborted = sum(r['safe_abort'] for r in rows)
        spent = sum(r['verification_cost'] for r in rows)
        # Lexicographic objective fixed before running: unsafe, safe-abort, cost, stages.
        outcomes.append((unsafe, aborted, round(spent, 8), positions))
    return min(outcomes)[-1], sorted(outcomes)[:5]
