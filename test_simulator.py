import unittest
from dataclasses import replace
from src.simulator import Case, intended_state, inject_fault, rule_verifier, evidence_verifier, simulate, generate_cases, optimize_positions

class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.ok = Case('x', 'retrieval_heavy', 300, 2, False, -1, 'none', -1, 0.0, 0.3)

    def test_clean_case_no_false_alarm(self):
        for positions in [(), (0, 1, 2, 3, 4, 5, 6)]:
            for kind in ['rule', 'evidence', 'heterogeneous']:
                r = simulate(self.ok, positions, kind)
                self.assertEqual((r['success'], r['unsafe'], r['safe_abort']), (1, 0, 0))

    def test_silent_faults_preserve_schema_and_become_wrong(self):
        for name in ('destination','permission','quantity','sku','price','stock','evidence'):
            c = replace(self.ok, faulty=True, fault_stage=2, fault_type=name, deadline=2)
            changed = inject_fault(intended_state(c), c)
            self.assertEqual(set(changed), set(intended_state(c)))
            self.assertFalse(rule_verifier(changed,c) and evidence_verifier(changed,c))
            r = simulate(c, (2,), 'heterogeneous')
            self.assertEqual((r['detected'], r['success'], r['unsafe']), (1, 1, 0))

    def test_verifier_scope_independence(self):
        c = replace(self.ok, faulty=True, fault_stage=2, fault_type='sku', deadline=2)
        bad = inject_fault(intended_state(c),c)
        self.assertTrue(rule_verifier(bad,c))
        self.assertFalse(evidence_verifier(bad,c))
        c2 = replace(c, fault_type='price')
        bad2 = inject_fault(intended_state(c2),c2)
        self.assertFalse(rule_verifier(bad2,c2))
        self.assertTrue(evidence_verifier(bad2,c2))

    def test_deadline_and_repair_abort(self):
        c = replace(self.ok, faulty=True, fault_stage=2, fault_type='sku', deadline=2, repair_uniform=0.99)
        self.assertEqual(simulate(c, (2,), 'heterogeneous')['safe_abort'], 1)
        self.assertEqual(simulate(c, (3,), 'heterogeneous')['unsafe'], 1)
        self.assertEqual(simulate(c, (), 'heterogeneous')['unsafe'], 1)

    def test_reproducibility_and_optimizer(self):
        a, b = generate_cases(4, 50, 'dev'), generate_cases(4, 50, 'dev')
        self.assertEqual(a, b)
        result, _ = optimize_positions(a)
        self.assertEqual(len(result),3)
        self.assertEqual(len(set(result)),3)

if __name__ == '__main__':
    unittest.main()
