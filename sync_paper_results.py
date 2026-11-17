"""Regenerate LaTeX numerical macros solely from measured result files.

Run after scripts/evaluate.py and before compiling paper/main.tex.
"""
from pathlib import Path
import json
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = pd.read_csv(ROOT/'results'/'results.csv').set_index('method')
PAIRS = json.loads((ROOT/'results'/'paired_comparison.json').read_text())
NAMES = {
 'none':'None', 'final_only':'FinalOnly', 'periodic':'Periodic',
 'global_risk':'GlobalRisk', 'profile_adaptive':'ProfileAdaptive',
 'adaptive_rule_only':'AdaptiveRuleOnly','adaptive_evidence_only':'AdaptiveEvidenceOnly'
}
values = {}
for row, prefix in NAMES.items():
    for col, suffix in [('unsafe_rate','Unsafe'),('task_success_rate','Success'),
                         ('safe_abort_rate','Abort'),('fault_detection_rate','Detection')]:
        values[f'{prefix}{suffix}'] = f'{100*DATA.loc[row,col]:.2f}'
    values[f'{prefix}Cost']=f"{DATA.loc[row,'mean_verification_cost_units']:.2f}"
comp = PAIRS[0]
values['PairedDelta'] = f"{comp['delta_unsafe_pp']:.2f}"
values['PairedLo'] = f"{comp['paired_bootstrap_95pct_pp'][0]:.2f}"
values['PairedHi'] = f"{comp['paired_bootstrap_95pct_pp'][1]:.2f}"
text = ('% GENERATED from measured CSV and paired JSON; do not hand-edit statistics.\n'
        + ''.join(f'\\newcommand{{\\res{k}}}{{{v}}}\n' for k,v in values.items()))
(ROOT/'paper'/'numbers.tex').write_text(text)
print(f"Synchronized {len(values)} LaTeX result macros")
