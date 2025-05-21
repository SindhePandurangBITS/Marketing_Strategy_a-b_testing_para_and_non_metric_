"""Non-parametric tests"""

import pandas as pd
from scipy.stats import fisher_exact, kruskal, mannwhitneyu
from itertools import combinations


def fisher_exact_test(ab):
    """Fisher"""
    cont = pd.crosstab(ab['group'], ab['outcome'])
    table = [
        [cont.loc['treatment', 1], cont.loc['treatment', 0]],
        [cont.loc['control', 1], cont.loc['control', 0]],
    ]
    orr, p = fisher_exact(table)
    print("Fisher's test", table, "OR:", round(orr,4), "p:", round(p,4))


def kruskal_wallis_test(ab):
    """Kruskal-Wallis"""
    t = ab[ab['group'] == 'treatment']
    data = [g['outcome'].values for _, g in t.groupby('marketing_strategy')]
    stat, p = kruskal(*data)
    print("K-W H-test", "H:", round(stat,4), "p:", round(p,4))


def mann_whitney_pairwise(ab):
    """Mann-Whitney U"""
    t = ab[ab['group'] == 'treatment']
    grouped = t.groupby('marketing_strategy')['outcome'].apply(list)
    wins = {k: 0 for k in grouped.index}
    for a, b in combinations(grouped.index, 2):
        _, p_ab = mannwhitneyu(grouped[a], grouped[b], alternative='greater')
        if p_ab < 0.05:
            wins[a] += 1
        _, p_ba = mannwhitneyu(grouped[b], grouped[a], alternative='greater')
        if p_ba < 0.05:
            wins[b] += 1
    df = pd.DataFrame(wins.items(), columns=['strategy','wins']).sort_values('wins', ascending=False)
    print("Best by wins:")
    print(df)
