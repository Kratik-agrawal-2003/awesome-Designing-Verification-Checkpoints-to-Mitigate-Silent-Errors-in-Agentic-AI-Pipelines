"""Actual paired simulated trials; every trial/method outcome is saved to CSV."""
import argparse
import csv
import json
import platform
import sys
import time
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.simulator import generate_cases, optimize_positions, simulate, PROFILES


def save_csv(file, rows, fields=None):
    rows = list(rows)
    file.parent.mkdir(parents=True, exist_ok=True)
    fields = fields or list(rows[0].keys())
    with file.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default=str(ROOT / 'configs' / 'frozen_protocol.json'))
    parser.add_argument('--out', default=str(ROOT / 'results'))
    args = parser.parse_args()
    cfg = json.loads(Path(args.config).read_text())
    out = Path(args.out)
    out.mkdir(exist_ok=True, parents=True)
    start = time.perf_counter()
    dev = generate_cases(cfg['dev_seed'], cfg['dev_cases_total'], 'dev')
    # Keep the generator's profile labels, not an artificially filtered sample.
    global_positions, global_top = optimize_positions(dev)
    per_profile = {}
    for p in PROFILES:
        per_profile[p], _ = optimize_positions([c for c in dev if c.profile == p])
    choices = {
        'none': ((), 'heterogeneous'),
        'final_only': ((6,), 'heterogeneous'),
        'periodic': (tuple(cfg['baseline_periodic_positions']), 'heterogeneous'),
        'global_risk': (global_positions, 'heterogeneous'),
        'profile_adaptive': (None, 'heterogeneous'),
        'adaptive_rule_only': (None, 'rule'),
        'adaptive_evidence_only': (None, 'evidence'),
    }
    cases = []
    records = []
    sensitivity = []
    for seed in cfg['test_seeds']:
        test = generate_cases(seed, cfg['test_cases_per_seed'], 'test')
        for case in test:
            # A strict data split is guaranteed by prefix and distinct seeds.
            assert case.case_id.startswith('test-')
            cases.append(asdict(case))
            for method, (positions, kind) in choices.items():
                positions = tuple(per_profile[case.profile]) if positions is None else positions
                row = simulate(case, positions, kind)
                records.append(dict(method=method, seed=seed, positions='-'.join(map(str, positions)), **row))
            # Perturb only the policy-routing label. Physical fault profile remains unchanged.
            other = PROFILES[1 - PROFILES.index(case.profile)]
            for p in cfg['routing_noise_sensitivity']:
                row = simulate(case, tuple(per_profile[case.profile]), 'heterogeneous',
                               route_flip_probability=float(p), alternate_positions=tuple(per_profile[other]))
                sensitivity.append(dict(noise_probability=p, seed=seed, **row))
    save_csv(out / 'dev_scenarios.csv', [asdict(c) for c in dev])
    save_csv(out / 'test_scenarios.csv', cases)
    save_csv(out / 'trial_outcomes.csv', records)
    save_csv(out / 'routing_sensitivity_trials.csv', sensitivity)
    metadata = {
        'python': platform.python_version(), 'platform': platform.platform(),
        'elapsed_wall_seconds': round(time.perf_counter() - start, 2),
        'development_sample_count': len(dev), 'test_sample_count': len(cases),
        'development_only_global_selection': list(global_positions),
        'development_only_profile_selection': {p: list(v) for p, v in per_profile.items()},
        'development_top5_global_unsafe_aborted_cost_positions': [list(x[:3]) + [list(x[3])] for x in global_top],
        'test_case_ids_start': cases[0]['case_id'],
        'test_case_ids_end': cases[-1]['case_id'],
        'frozen_protocol': cfg,
    }
    (out / 'run_metadata.json').write_text(json.dumps(metadata, indent=2))
    print(json.dumps({k: v for k, v in metadata.items() if k != 'frozen_protocol'}, indent=2))

if __name__ == '__main__':
    run()
