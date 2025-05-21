

---

# 📊 Marketing Strategy Optimization – A/B Testing (Parametric & Non-Parametric)


[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/your_username/ab-testing-project.svg)](https://github.com/your_username/ab-testing-project/stargazers)
[![Dataset: UCI Bank Marketing](https://img.shields.io/badge/Dataset-UCI%20Bank%20Marketing-orange.svg)](https://archive.ics.uci.edu/ml/datasets/bank+marketing)


---

## 🎯 Business Challenge

Identify which marketing contact strategies drive the most customer conversions. This project simulates a real-world A/B test by comparing contacted (treatment) vs. non-contacted (control) users to measure and rank strategy performance.

---

## ✅ Tests Covered (Parametric & Non-Parametric)

This project evaluates strategy effectiveness using:

* **Parametric**: ANOVA, Welch’s t-test, Tukey’s HSD, Chi-square, Z-test, Bayesian A/B Test
* **Non-Parametric**: Kruskal–Wallis, Mann–Whitney U, Fisher’s Exact
  Diagnostic checks ensure correct test selection based on data assumptions.

---

## ❓ Why Use Both Parametric & Non-Parametric Tests?

Using both ensures valid conclusions regardless of data shape. When assumptions like normality or variance equality break, non-parametric methods still yield robust results.

---

## 🧪 Test Mapping to Business Questions

| **Assumption Type**          | **Comparison Type**  | **Goal**                    | **Test(s)**                       |
| ---------------------------- | -------------------- | --------------------------- | --------------------------------- |
| Parametric (Valid)           | Treatment vs Control | Overall Effectiveness       | Chi-square, Z-test, Bayesian Test |
| Non-Parametric               | Treatment vs Control | Assumption-Free Comparison  | Fisher’s Exact, Kruskal–Wallis    |
| Parametric (Partially Valid) | Strategy Comparisons | Top Strategy Identification | ANOVA, Welch’s t-test, Tukey HSD  |
| Non-Parametric               | Strategy Comparisons | Top Strategy (Non-normal)   | Mann–Whitney U                    |

---

## 📊 Test Summary

| **Test**          | **H₀**                      | **H₁**                    | **Key Findings**                                                           |
| ----------------- | --------------------------- | ------------------------- | -------------------------------------------------------------------------- |
| Chi-Square        | T = C success rates         | T ≠ C success rates       | 9/10 strategies show lift; Welcome Calls leads; Cellular underperforms     |
| Bayesian A/B      | All strategies equal        | At least one different    | Welcome Calls P(best) ≈ 0.744; Festive ≈ 0.253                             |
| Z-Test (Pairwise) | Proportions equal           | Proportions differ        | Most p < 0.001; Welcome Calls best; Cellular & Telephone lowest performers |
| Fisher’s Exact    | T = C success rates         | T ≠ C                     | p = 0.0000; Treatment converts 2.4× better                                 |
| Kruskal–Wallis    | All strategies same         | At least one different    | Significant strategy differences (p = 0.0000)                              |
| Mann–Whitney U    | Strategy i = j distribution | One outperforms the other | Welcome Calls wins 8/10; Festive & Voice strong; Cellular worst            |
| ANOVA             | All means equal             | At least one mean differs | Welcome (74.4%) and Festive (25.3%) dominate                               |
| Welch’s t-test    | Meanᵢ = Meanⱼ               | Meanᵢ ≠ Meanⱼ             | Most p ≪ 0.001; strong pairwise contrasts                                  |
| Tukey’s HSD       | μᵢ = μⱼ                     | μᵢ ≠ μⱼ                   | Welcome better than all; Festive similar to Welcome (p-adj ≈ 0.51)         |

---

## 🏁 Final Results

| **Insight**         | **Summary**                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| Treatment Effective | All tests show treatment group outperforms control—marketing contact works. |
| Strategies Differ   | Strong evidence that strategies are not equally effective.                  |
| Welcome Calls Win   | Consistently top-performing strategy across all test types.                 |

---

## 🧬 Project Pipeline

1. **Business Understanding** – Define goals, target conversions, top outreach strategy.
2. **Data Wrangling** – Load, clean, and assign treatment/control using `poutcome`.
3. **Preprocessing** – Encode outcomes, fix dates, drop leakage.
4. **EDA** – Plot group-wise conversions and strategy balance.
5. **Diagnostics** – Validate assumptions (normality, variance).
6. **Parametric Tests (Valid)** – Chi-square, Z-test, Bayesian (assumptions met).
7. **Non-Parametric Tests** – Fisher, Kruskal–Wallis, Mann–Whitney (no assumptions).
8. **Parametric Tests (Partial Validity)** – ANOVA, Welch, Tukey (via CLT).
9. **Findings** – Welcome Calls dominate; strategies vary.
10. **Future Scope** – Add cost-per-conversion, time-based A/B, uplift models.

---

## 🔧 Installation & Quick Start

```bash
# Clone repo
git clone https://github.com/SindhePandurangBITS/ab-testing-project.git
cd ab-testing-project

# Setup environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run pipeline
python src/data_loader.py --input data_raw/ab_data.csv --output data_processed/clean.csv
python src/preprocessing.py --input data_processed/clean.csv --output data_processed/preprocessed.csv
python src/EDA.py --input data_processed/preprocessed.csv
python src/diagnostics.py --input data_processed/preprocessed.csv
python src/tests_parametric_valid.py --input data_processed/preprocessed.csv
python src/tests_parametric_partially_valid.py --input data_processed/preprocessed.csv
python src/tests_nonparametric.py --input data_processed/preprocessed.csv
```

---

## 📖 Documentation

All detailed code and findings are in:
`notebooks/AB_testing(para_and_non_parametric).ipynb`

---

## 🗂 Key References

1. **Kohavi, R. et al. (2009)**
   *Controlled Experiments on the Web: Survey and Practical Guide*
   [DOI:10.1007/s10618-008-0114-1](https://doi.org/10.1007/s10618-008-0114-1)

2. **NASSCOM & Zinnov (2020)**
   *Marketing Analytics in India – Unlocking the Power of Data*
   [nasscom.in/publications/marketing-analytics](https://nasscom.in/knowledge-center/publications/marketing-analytics-india-unlocking-power-data)

---

## ⭐ Support

If this project helped you, please consider giving it a ⭐ and sharing it with your network!

---

