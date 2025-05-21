import pandas as pd
import matplotlib.pyplot as plt
import itertools
from scipy.stats import shapiro, levene
import statsmodels.api as sm
from statsmodels.formula.api import ols


def qq_plot(residuals):
    """QQ plot"""
    sm.qqplot(residuals, line='s')
    plt.title("Q-Q Plot of Residuals")
    plt.show()


def shapiro_wilk_test(df, group_col, outcome_col):
    """Shapiro-Wilk per group"""
    results = {}
    for name, grp in df.groupby(group_col):
        stat, p = shapiro(grp[outcome_col])
        results[name] = p
        print(f"{name}: p = {p:.4f}")
    return results


def levene_test(df, group_col, outcome_col):
    """Levene's test"""
    groups = [grp[outcome_col].values for _, grp in df.groupby(group_col)]
    stat, p = levene(*groups)
    print(f"Levene's test p = {p:.4f}")
    return p


def residuals_diagnostics(df, formula):
    """ANOVA residuals"""
    model = ols(formula, data=df).fit()
    resid = model.resid
    stat, p = shapiro(resid)
    print(f"Shapiro-Wilk p = {p:.4f}")
    qq_plot(resid)
    return resid, p


def normal_approximation(df, group_col, outcome_col):
    """Normal approx check"""
    data = {name: grp[outcome_col].values for name, grp in df.groupby(group_col)}
    checks = []
    for a, b in itertools.combinations(data, 2):
        g1, g2 = data[a], data[b]
        n1, x1 = len(g1), g1.sum()
        n2, x2 = len(g2), g2.sum()
        p1, p2 = x1/n1, x2/n2
        cond = all([n1*p1>=5, n1*(1-p1)>=5, n2*p2>=5, n2*(1-p2)>=5])
        checks.append({
            'grp1': a, 'grp2': b,
            'n1*p1': round(n1*p1,2), 'n1*(1-p1)': round(n1*(1-p1),2),
            'n2*p2': round(n2*p2,2), 'n2*(1-p2)': round(n2*(1-p2),2),
            'cond_met': cond
        })
    return pd.DataFrame(checks)
