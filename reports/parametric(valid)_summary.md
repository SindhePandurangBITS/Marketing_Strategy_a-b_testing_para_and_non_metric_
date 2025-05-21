
### Summary of Parametric (Assumptions - Valid) Test Results 


| **Test**             | **Hypotheses**                                                                                                     | **Key Findings**                                                                                                     | **Recommendation**                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Chi-Square Test**  | H₀: Treatment and control have equal success rates<br>H₁: Success rates differ                                     | 9 out of 10 strategies show significant lift (p < 0.001), “Welcome calls” leads, “cellular” shows negative lift       | Prioritize high-lift strategies, avoid “cellular”   |
| **Bayesian A/B Test**| H₀: All strategies have the same true conversion rate<br>H₁: At least one strategy has a different true rate        | **Welcome Calls** has P(best) ≈ 0.744, **Festive Offers** ≈ 0.253, others ≈ 0                                          | Focus on top two strategies with high posterior prob|
| **Pairwise Z-Test**  | H₀: pᵢ = pⱼ (equal success rates)<br>H₁: pᵢ ≠ pⱼ (different success rates)                                          | Most p-values < 0.001; **Welcome Calls** clearly leads, **Cellular** and **Telephone** underperform consistently       | Use Z-test to reinforce best/worst strategy choices |
