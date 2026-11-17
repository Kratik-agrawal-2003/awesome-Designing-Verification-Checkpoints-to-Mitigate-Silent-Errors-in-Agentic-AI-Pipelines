"""Validates rows against generated test cases, aggregates real CSV, saves paper figures."""
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'results'
METHODS = ['none','final_only','periodic','global_risk','profile_adaptive',
           'adaptive_rule_only','adaptive_evidence_only']

def bootstrap_paired_difference(wide, a, b, seed=724, reps=1200):
    # Paired across the same case IDs; interval characterizes sample variability,
    # not uncertainty about simulator assumptions or out-of-distribution behavior.
    rng = np.random.default_rng(seed)
    v = (wide[a] - wide[b]).to_numpy(dtype=float)
    n = len(v)
    observed = float(v.mean())
    boots = [float(np.mean(v[rng.integers(0,n,n)])) for _ in range(reps)]
    lo, hi = np.quantile(boots, [0.025,0.975])
    return {'contrast': f'{a} minus {b}', 'delta_unsafe_pp': round(100*observed,3),
            'paired_bootstrap_95pct_pp': [round(100*lo,3),round(100*hi,3)], 'resamples':reps}

def main():
    df = pd.read_csv(RES / 'trial_outcomes.csv')
    cases = pd.read_csv(RES / 'test_scenarios.csv')
    sens = pd.read_csv(RES / 'routing_sensitivity_trials.csv')
    # Empty checkpoint schedules are serialized as an empty CSV cell; pandas
    # reads it as NaN. That is a valid no-checkpoint policy, not missing data.
    df['positions'] = df['positions'].fillna('')
    assert not df.isna().any().any() and not cases.isna().any().any()
    assert set(df['method']) == set(METHODS)
    assert len(df) == len(cases)*len(METHODS)
    assert not df.duplicated(['case_id','method']).any()
    assert cases['case_id'].is_unique
    assert set(df.case_id) == set(cases.case_id)
    assert all(df['success'] + df['unsafe'] + df['safe_abort'] == 1)
    assert all(df['detected'] <= df['faulty'])
    assert not set(df.case_id).intersection(set(pd.read_csv(RES/'dev_scenarios.csv').case_id))
    piv = df.pivot(index='case_id', columns='method', values='unsafe')[METHODS]
    rows=[]
    for name in METHODS:
        d = df[df.method == name]
        fault = d[d.faulty == 1]
        rows.append({
            'method': name,'n_cases':len(d),'n_faults':len(fault),
            'unsafe_rate':float(d.unsafe.mean()),
            'task_success_rate':float(d.success.mean()),
            'safe_abort_rate':float(d.safe_abort.mean()),
            'fault_detection_rate':float(fault.detected.mean()),
            'mean_verification_cost_units':float(d.verification_cost.mean()),
            'mean_checks':float(d.checks.mean()),
            'mean_detection_lag_stages':float(fault.loc[fault.detected==1,'detection_lag'].mean())
              if fault.detected.sum() else None
        })
    table=pd.DataFrame(rows)
    table.to_csv(RES/'results.csv',index=False,float_format='%.6f')
    seed_table = df.groupby(['seed','method']).agg(unsafe_rate=('unsafe','mean'),
        success_rate=('success','mean'),mean_verification_cost_units=('verification_cost','mean')).reset_index()
    seed_table.to_csv(RES/'per_seed_results.csv', index=False)
    sensitivity=sens.groupby('noise_probability').agg(
        unsafe_rate=('unsafe','mean'),task_success_rate=('success','mean'),
        mean_verification_cost_units=('verification_cost','mean')).reset_index()
    sensitivity.to_csv(RES/'routing_sensitivity.csv',index=False)
    pairs = [bootstrap_paired_difference(piv,'periodic','profile_adaptive'),
             bootstrap_paired_difference(piv,'global_risk','profile_adaptive'),
             bootstrap_paired_difference(piv,'periodic','global_risk')]
    (RES/'paired_comparison.json').write_text(json.dumps(pairs,indent=2))
    stage = (df[(df.faulty == 1) & df.method.isin(['periodic','global_risk'])]
             .groupby(['fault_stage','method']).agg(n=('unsafe','size'),
                                                     unsafe_rate=('unsafe','mean'))
             .reset_index())
    stage.to_csv(RES/'stage_failure_analysis.csv',index=False)
    # Four figures from actual results, no illustrative percentages.
    plt.rcParams.update({'font.size':10,'figure.dpi':140})
    fig, ax=plt.subplots(figsize=(8.0,4.2))
    titles=['No checks','Final only','Periodic','Global risk','Adaptive','Adaptive/rules','Adaptive/evidence']
    ax.bar(range(len(table)),100*table.unsafe_rate)
    ax.set_xticks(range(len(table)),titles,rotation=28,ha='right')
    ax.set_ylabel('Unsafe terminal outcomes (% of cases)')
    ax.set_title('Held-out synthetic experiment (five paired seeds)')
    ax.set_ylim(0,max(1,100*table.unsafe_rate.max()*1.12))
    fig.tight_layout()
    for folder in [RES/'figures',ROOT/'paper'/'figures']:
        folder.mkdir(exist_ok=True, parents=True)
        fig.savefig(folder/'unsafe_outcomes.png',dpi=200)
        fig.savefig(folder/'unsafe_outcomes.pdf')
    plt.close(fig)
    fig, ax=plt.subplots(figsize=(6.7,4.1))
    d=table.loc[table.method != 'none']
    for _,r in d.iterrows():
        ax.scatter(r.mean_verification_cost_units,100*r.unsafe_rate,s=48)
        ax.annotate(r.method.replace('_',' '),(r.mean_verification_cost_units,100*r.unsafe_rate),
                    xytext=(5,4),textcoords='offset points',fontsize=8)
    ax.set_xlabel('Mean verification cost (abstract units/case)')
    ax.set_ylabel('Unsafe outcomes (%)')
    ax.set_title('Failure-versus-checking cost trade-off')
    ax.grid(alpha=0.2)
    fig.tight_layout()
    for folder in [RES/'figures',ROOT/'paper'/'figures']:
        fig.savefig(folder/'cost_tradeoff.png',dpi=200)
        fig.savefig(folder/'cost_tradeoff.pdf')
    plt.close(fig)
    fig, ax=plt.subplots(figsize=(6.3,3.7))
    ax.plot(100*sensitivity.noise_probability,100*sensitivity.unsafe_rate,marker='o')
    ax.set_xlabel('Adaptive context misrouting probability (%)')
    ax.set_ylabel('Unsafe outcomes (%)')
    ax.set_title('Sensitivity to imperfect context routing')
    ax.grid(alpha=0.2)
    fig.tight_layout()
    for folder in [RES/'figures',ROOT/'paper'/'figures']:
        fig.savefig(folder/'routing_sensitivity.png',dpi=200)
        fig.savefig(folder/'routing_sensitivity.pdf')
    plt.close(fig)
    fig, ax=plt.subplots(figsize=(7.0,3.7))
    x=np.arange(7)
    for shift,method,label in [(-0.19,'periodic','Periodic (1,3,5)'),
                               (0.19,'global_risk','Selected (2,4,6)')]:
        vals=stage[stage.method==method].sort_values('fault_stage').unsafe_rate.to_numpy()
        ax.bar(x+shift,100*vals,width=0.37,label=label)
    ax.set_xticks(x,[f'{i}' for i in x])
    ax.set_xlabel('Injected fault stage (0 = intent, 6 = pre-action)')
    ax.set_ylabel('Unsafe outcomes among faulty cases (%)')
    ax.set_title('Which fault locations each schedule fails to contain')
    ax.legend(fontsize=8)
    ax.set_ylim(0,105)
    fig.tight_layout()
    for folder in [RES/'figures',ROOT/'paper'/'figures']:
        fig.savefig(folder/'stage_failure_analysis.png',dpi=200)
        fig.savefig(folder/'stage_failure_analysis.pdf')
    plt.close(fig)
    print(table.to_string(index=False,float_format=lambda x:f'{x:.4f}'))
    print('\nPaired contrasts:',json.dumps(pairs,indent=2))
    print('\nRouting sensitivity:',sensitivity.to_string(index=False))

if __name__=='__main__':
    main()
