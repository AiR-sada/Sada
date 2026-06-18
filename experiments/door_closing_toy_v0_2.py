#!/usr/bin/env python3
"""
Door-Closing Toy v0.2

Single-shot exact enumeration. A powerful actor A can close another actor B's future
options ("doors"), delete B's contestability logs, or fix a hazard that would close
B's doors by omission. The crux: closing B's doors does not reduce A's own
reachability. This makes self-protection insufficient to protect B.

Outputs:
  - stdout table
  - <out_dir>/door_closing_toy_results.json
  - <out_dir>/door_closing_toy.png
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D_B, H, C_FIX, EPS_LOG = 10, 4, 2.0, 1.0
BETA = GAMMA = 1.5
CLOSE = [0,2,4,6,8,10]
OBJS = [
    'RewardMax','AUP_self','RR_stepwise_inaction','RR_startstate',
    'Patency_commission','Patency_omission'
]


def outcome(cB, fix, dlog, lam):
    omission = 0 if fix else H
    b_doors = max(0, D_B - cB - omission)
    a_reward = lam*cB + EPS_LOG*dlog - C_FIX*fix
    commission = cB + dlog
    total = commission + omission
    return dict(cB=cB, fix=fix, dlog=dlog, omission=omission, b_doors=b_doors,
                a_reward=a_reward, commission=commission, total=total)


def score(obj, o):
    r = o['a_reward']
    dA_self = 0.0
    return {
        'RewardMax': r,
        'AUP_self': r - BETA*abs(dA_self),
        'RR_stepwise_inaction': r - BETA*o['commission'],
        'RR_startstate': r - BETA*o['total'],
        'Patency_commission': r - GAMMA*o['commission'],
        'Patency_omission': r - GAMMA*o['total'],
    }[obj]


def best(obj, lam):
    bo = None
    for cB, fx, dl in itertools.product(CLOSE, [0,1], [0,1]):
        o = outcome(cB, fx, dl, lam)
        s = score(obj, o)
        if bo is None or s > bo[0] + 1e-9:
            bo = (s, o)
    return bo[1]


def threshold(obj, lams):
    for lam in lams:
        if best(obj, lam)['cB'] > 0:
            return float(lam)
    return None


def run(out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    lams = np.round(np.arange(0, 3.01, 0.25), 2)
    curves = {o: [] for o in OBJS}
    table = []
    print(f"{'lam':>5} | " + ' | '.join(f"{o[:10]:>10}" for o in OBJS) + '   (B doors surviving)')
    print('-'*100)
    for lam in lams:
        row = {'lam': float(lam)}
        display = []
        for o in OBJS:
            b = best(o, lam)
            curves[o].append(b['b_doors'])
            row[o] = dict(b)
            display.append(f"{b['b_doors']:>10}")
        table.append(row)
        print(f"{lam:>5} | " + ' | '.join(display))

    print('\n--- behaviour at low temptation (lam=0.5) ---')
    low = {}
    for o in OBJS:
        b = best(o, 0.5); low[o] = dict(b)
        print(f"{o:>22}: close_B={b['cB']}  fix_hazard={b['fix']}  delete_logs={b['dlog']}  -> B keeps {b['b_doors']}/10")

    print('\n--- temptation threshold where each agent STARTS forcibly closing B\'s doors ---')
    thresholds = {}
    for o in OBJS:
        thresholds[o] = threshold(o, lams)
        print(f"{o:>22}: lam* = {thresholds[o]}")

    sig = {o: tuple((best(o, float(l))['cB'], best(o, float(l))['fix'], best(o, float(l))['dlog']) for l in lams) for o in OBJS}
    seen = {}
    for o in OBJS:
        seen.setdefault(sig[o], []).append(o)
    equivalences = [grp for grp in seen.values() if len(grp) > 1]
    print('\n--- behavioural equivalences across the sweep ---')
    for grp in equivalences:
        print('  IDENTICAL behaviour:  ' + '  ==  '.join(grp))

    plt.figure(figsize=(8,5))
    styles = {'RewardMax':'-','AUP_self':'--','RR_stepwise_inaction':'-.','RR_startstate':':',
              'Patency_commission':'-.','Patency_omission':':'}
    for o in OBJS:
        plt.plot(lams, curves[o], styles.get(o, '-'), lw=2.2, label=o, alpha=.8)
    plt.xlabel('temptation lam (A reward per B-door closed)')
    plt.ylabel("B's surviving doors (out of 10)")
    plt.title('Door-Closing Toy v0.2 - who protects B, and until what temptation')
    plt.legend(fontsize=8)
    plt.grid(alpha=.3)
    plt.tight_layout()
    fig_path = out_dir / 'door_closing_toy.png'
    plt.savefig(fig_path, dpi=130)

    result = {
        'version': '0.2',
        'parameters': {'D_B': D_B, 'H': H, 'C_FIX': C_FIX, 'EPS_LOG': EPS_LOG, 'BETA': BETA, 'GAMMA': GAMMA},
        'lams': [float(x) for x in lams],
        'thresholds': thresholds,
        'low_temptation_lam_0_5': low,
        'equivalences': equivalences,
        'summary': {
            'rewardmax_equals_aup_self': ['RewardMax','AUP_self'] in equivalences,
            'patency_commission_equals_rr_stepwise_inaction': ['RR_stepwise_inaction','Patency_commission'] in equivalences or ['Patency_commission','RR_stepwise_inaction'] in equivalences,
            'patency_omission_equals_rr_startstate': ['RR_startstate','Patency_omission'] in equivalences or ['Patency_omission','RR_startstate'] in equivalences,
            'penalty_threshold_lam': thresholds['Patency_commission'],
            'negative_result': 'Penalty-style option preservation collapses when temptation exceeds the penalty; structural authority caps are motivated.'
        },
        'table': table,
        'figure': str(fig_path.name),
    }
    (out_dir/'door_closing_toy_results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"\nsaved figure: {fig_path}")
    print(f"saved results: {out_dir/'door_closing_toy_results.json'}")
    return result


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='outputs')
    args = ap.parse_args()
    run(Path(args.out_dir))
