import pandas as pd
from scipy.stats import f_oneway, ttest_ind
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from itertools import combinations

def one_way_anova(ab):
    """One-way ANOVA"""
    df = ab[ab['group']=='treatment']  # filter
    groups = [g['outcome'].values for _, g in df.groupby('marketing_strategy')]
    f, p = f_oneway(*groups)  # compute
    print(f"F={f:.4f}, p={p:.4f}")

def pairwise_ttest(ab):
    """Pairwise Welch t-tests"""
    df = ab[ab['group']=='treatment']  # filter
    groups = {n: g['outcome'].values for n, g in df.groupby('marketing_strategy')}
    for a, b in combinations(groups, 2):
        t, p = ttest_ind(groups[a], groups[b], equal_var=False)  # compute
        print(f"{a} vs {b}: t={t:.4f}, p={p:.4f}")

def tukey_hsd(ab):
    """Tukey HSD"""
    df = ab[ab['group']=='treatment'][['marketing_strategy', 'outcome']]  # filter
    res = pairwise_tukeyhsd(endog=df['outcome'], groups=df['marketing_strategy'], alpha=0.05)
    df_res = pd.DataFrame(res.summary().data[1:], columns=res.summary().data[0])  # parse
    return df_res.sort_values('p-adj')  # sort

if __name__ == "__main__":
    ab = pd.read_csv('src/ab_data.csv')  # load data
    print("ANOVA"); one_way_anova(ab)
    print("\nT-tests"); pairwise_ttest(ab)
    print("\nTukey HSD"); print(tukey_hsd(ab))
