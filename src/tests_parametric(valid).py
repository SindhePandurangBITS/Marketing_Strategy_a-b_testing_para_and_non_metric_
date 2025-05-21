"""
Parametric tests (valid assumptions) for A/B analysis
"""

import sys
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, beta, norm
from itertools import combinations


def chi_square_test(ab, control):
    """Chi-square 2x2 test"""
    results = []
    for method in ab['marketing_strategy'].unique():
        tr = ab[(ab['group'] == 'treatment') & (ab['marketing_strategy'] == method)]
        if tr.empty:
            continue
        s1 = tr['outcome'].sum()
        n1 = len(tr)
        s2 = control['outcome'].sum()
        n2 = len(control)
        if n1 == 0 or n2 == 0:
            continue
        table = [[s1, n1 - s1], [s2, n2 - s2]]
        chi2, p, _, _ = chi2_contingency(table)
        if p < 0.05:
            if s1/n1 > s2/n2:
                st = "Better"
            elif s1/n1 < s2/n2:
                st = "Worse"
            else:
                st = "Same"
        else:
            st = "No diff"
        results.append({
            'strategy': method,
            'tr_rate': round(s1/n1, 4),
            'ctrl_rate': round(s2/n2, 4),
            'p': round(p, 4),
            'res': st
        })
    return pd.DataFrame(results).sort_values('p')


def bayesian_test(ab, samples=10000):
    """Bayes beta-binomial MC"""
    tr = ab[ab['group'] == 'treatment']
    posts = {}
    for name, grp in tr.groupby('marketing_strategy')['outcome']:
        s = grp.sum()
        n = len(grp)
        posts[name] = beta(1 + s, 1 + n - s)
    draws = {k: v.rvs(samples) for k, v in posts.items()}
    arr = np.array([draws[k] for k in draws])
    best = (arr == arr.max(axis=0)).sum(axis=1)
    probs = best / samples
    return dict(zip(posts.keys(), np.round(probs, 3)))


def pairwise_z_test(ab):
    """Pairwise z-test props"""
    tr = ab[ab['group'] == 'treatment']
    outs = {name: grp['outcome'].values for name, grp in tr.groupby('marketing_strategy')}
    res = []
    for a, b in combinations(outs, 2):
        x1, n1 = outs[a].sum(), len(outs[a])
        x2, n2 = outs[b].sum(), len(outs[b])
        p_pool = (x1 + x2) / (n1 + n2)
        se = (p_pool * (1 - p_pool) * (1/n1 + 1/n2))**.5
        z = 0 if se == 0 else (x1/n1 - x2/n2) / se
        pval = 1.0 if se == 0 else 2 * (1 - norm.cdf(abs(z)))
        res.append({
            'm1': a,
            'm2': b,
            'p1': round(x1/n1, 4),
            'p2': round(x2/n2, 4),
            'p': round(pval, 4)
        })
    return pd.DataFrame(res).sort_values('p')


if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])
    control = df[df['group'] == 'control']
    print(chi_square_test(df, control).head(15))
    print(bayesian_test(df))
    print(pairwise_z_test(df).head(50))
