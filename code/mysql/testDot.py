import re


def is_filter(ww):
    return ww.find("............") >= 0


# s = "Of the  patients studied, % had urine output> ml/day, .% were on high-flux HD and .% on HDF. Parameters most closely correlated with GFRResidual were /?-micoglobulin (r .) and /Cystatin C (r .). Both these relationships were weaker at low GFRResidual. The best regression model for GFRResidual, explaining % of the variation, was: GFRResidual = . · (/?m) - . Where ?m is the pre-dialysis ? microglobulin concentration (mg/L). This model was validated in a separate cohort of  patients using Bland-Altman analysis. Areas under the curve in Receiver Operating Characteristic analysis aimed at identifying subjects with urea clearance? ml/min/. m was . for ?-microglobulin and . for Cystatin C. A plasma ?-microglobulin cut-off of ?. mg/L allowed identification of patients with urea clearance ? ml/min/. m with % specificity and % sensitivity."
# s = "Thirty-five subjects enrolled and completed the protocol. At entry (median or %): age  years, % female, % non-white, % non-smokers, CD+ T cell count  cells/mm(), BMI  kg/m(). AT responses were heterogeneous, with statistically significant losses of median (IQR) total (TAT, .% (-., .), p = .) and subcutaneous (SAT, -.% (-., .), p = .) AT, but not VAT (-.% (-., .), p = .). Significant decreases in waist circumference and waist:hip ratio occurred (both p<.) without BMI or weight changes. In an exploratory analysis, significant increases in TNF-? occurred among female subjects without changes in other inflammatory or metabolic markers. No related adverse events occurred."
# s = "Dentine surfaces were etched with different concentrations of phosphoric acid (, , , ,  or wt%). Scanning electron microscopy was used to observe the micromorphology of the etched dentine surfaces. Energy dispersive X-ray analysis was performed to determine the residual Ca-content of the demineralised dentine matrix. Atomic force microscopy-based nanoindentation was used to analyse the nanomechanical properties of the treated dentine surfaces. The influence of HPO concentration on resin-dentine bond strength was evaluated by microtensile bond strength testing. One-way ANOVA was used to compare the residual Ca-content ratio, reduced elastic modulus (Er) of the treated dentine surfaces and microtensile bond strength among groups."
# s = "Compared with controls, athletes had a larger LV cavity (. (.) v . (.) mm), a difference of %. The LV cavity was >  mm in % athletes, whereas none of the controls had an LV cavity >  mm. The LV cavity exceeded predicted sizes in  (%) athletes. Among the athletes with LV dilatation, % were boys, LV size ranged from - mm, and left atrial diameter and LV wall thickness were enlarged. Systolic and diastolic function were normal. None of the athletes in the study had an LV cavity size >  mm. LV cavity size correlated with age, sex, heart rate, and body surface area."
# s = "There were significantly more patients with ACAs in the symptomatic subgroup compared to the screening or surveillance subgroup (.% vs .%, P<.; .% vs .%, P=.). No differences were found in the ACA frequency between the alarm and non-alarm categories (.% vs .%, P=.). One observation was that in the symptomatic subgroup, distal lesions were more likely to contain ACAs than proximal ones (OR ., % CI .-., P=.). It was also noted that nonpolypoid lesions had significantly higher amounts of ACAs in the symptomatic subgroup (OR ., % CI .-., P<.) than the other groups."
s = "With .% of offspring having consanguineous parents, the adjusted OR for major [birth defect] was . (.-.). Offspring of marriages between uncles-nieces, first cousins and more distant relatives showed adjusted ORs of . (.-.), . (.-.) and . (.-.) respectively. For descendents of grandfathers born in the same country, but not known to be related, the OR was . (.-.); these showed increased risk associated with ancestries in Western Asia (., .-., p < .) or Europe (., .-.)."
print(is_filter(s))
s = s.replace("%", "").replace(">", " ").replace("()", "") \
    .replace("[]", "").replace(" ± ", "").replace(", . ", " ").replace(
    "–)", ")").replace(".,", ",").replace("?-", "") \
    .replace("-?", "").replace("/", "").replace(". ·", "").replace("=", "").replace(
    "?.", "").replace(", ,", "").replace("(.)", "") \
    .replace("//", "").replace("<", "").replace("  ", " ") \
    .replace(" - ", "").replace(".-", " ").replace("...", "").replace("..", ".") \
    .replace("+-", "").replace("-.", "").replace(" . ", " ").replace("°", "")

print(s)
print(re.sub("\\([^()]*\\)", "", s))
print(len(s.split(" ")))
