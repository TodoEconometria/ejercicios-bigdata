# PCA Manual in Python: FactoMineR Style﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​‌‌​​​​‌‍​​‌‌​‌​​‍​‌‌​​​​‌‍​‌‌​​​‌‌‍​​‌‌​​​​‍​‌‌​​‌‌​‍​‌‌​​​‌‌﻿

## Replicating the Gold Standard of Multivariate Analysis

---

> ### Certification and Reference Information
>
> **Original author/Reference:** @TodoEconometria
> **Professor:** Juan Marcelo Gutierrez Miranda
> **Methodology:** Advanced Courses in Big Data, Data Science, AI Application Development & Applied Econometrics.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​‌‌​​​​‌‍​​‌‌​‌​​‍​‌‌​​​​‌‍​‌‌​​​‌‌‍​​‌‌​​​​‍​‌‌​​‌‌​‍​‌‌​​​‌‌﻿
> **Certification Hash ID:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
> **Repository:** [https://github.com/TodoEconometria/certificaciones](https://github.com/TodoEconometria/certificaciones)
>
> **MAIN ACADEMIC REFERENCE:**
>
> - Husson, F., Le, S., & Pages, J. (2017). *Exploratory Multivariate Analysis by Example Using R*. CRC Press.
> - **FactoMineR Tutorial:** [http://factominer.free.fr/course/FactoTuto.html](http://factominer.free.fr/course/FactoTuto.html)
> - Le, S., Josse, J., & Husson, F. (2008). FactoMineR: An R Package for Multivariate Analysis. *Journal of Statistical Software*, 25(1), 1-18.
> - Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *JMLR* 12, pp. 2825-2830.

---

## 1. Introduction: Why FactoMineR is the Gold Standard

### 1.1. The Problem of Multivariate Data

Imagine you have data from **41 athletes** who competed in the **decathlon** (10 sporting events). Each athlete has 10 measurements: race times, jump distances, and throwing distances. The question is: **How can we "see" patterns in 10 dimensions?**

The human brain can only visualize 2 or 3 dimensions. **Principal Component Analysis (PCA)** is the mathematical tool that allows us to "compress" those 10 dimensions into 2, losing as little information as possible.

### 1.2. Philosophy: FactoMineR vs. Scikit-Learn

This manual replicates the logic of **FactoMineR** (the gold standard in R) using Python.

| Aspect | Scikit-learn | FactoMineR / Prince |
|--------|--------------|---------------------|
| **Approach** | Machine Learning | **Data Exploration** |
| **Objective** | Reduce dimensions for a predictive model | **Understand which variables drive which individuals** |
| **Key metrics** | `explained_variance_ratio_` | **Contributions, $\cos^2$, correlations** |
| **Supplementary variables** | Not supported | **Native support** |
| **Plots** | Basic | **Correlation circle, biplot** |

> **The fundamental difference:** Scikit-learn tells you "these are your compressed data". FactoMineR tells you "**why** your data compressed this way, **which variables** are responsible, and **how reliable** the representation of each point is".

---

## 2. BEFORE STARTING: Missing Data Treatment

### 2.1. The Most Common Error: "I'll Just Plug in the Mean"

One of the most frequent errors in multivariate analysis is **imputing missing data with the mean without thinking**. This practice, although common, can **destroy the real structure of your data** and lead you to erroneous conclusions.

> **GOLDEN RULE:** Before imputing any missing value, **you must understand WHY that data is missing**. The imputation strategy depends on the **missingness mechanism**.

### 2.2. The Three Types of Missing Data (Rubin, 1976)

| Type | Name | Meaning | Example | Can we use the mean? |
|------|------|---------|---------|----------------------|
| **MCAR** | Missing Completely At Random | The data is missing **by pure chance**, unrelated to any variable | A sensor failed randomly | **YES**, but with caution |
| **MAR** | Missing At Random | The data is missing for a reason **related to OTHER observed variables** | Young people don't answer salary questions (but we know their age) | **DEPENDS** on the method |
| **MNAR** | Missing Not At Random | The data is missing for a reason **related to THE MISSING VALUE ITSELF** | The wealthy don't declare their assets BECAUSE they are high | **NO**, it biases the results |

### 2.3. Why the Mean Can Destroy Your Analysis

Imagine this scenario in the decathlon:

```
Athlete     | 100m  | Long Jump   | Throwing
------------|-------|-------------|------------
Sprinter A  | 10.5s | 7.8m        | ???
Sprinter B  | 10.7s | 7.6m        | ???
Thrower C   | 11.8s | 6.2m        | 18.5m
Thrower D   | 12.0s | 6.0m        | 19.2m
```

**Problem:** The sprinters (A and B) did not complete the throwing event (due to injury).

**If you impute with the throwing mean:**
- Throwing mean = (18.5 + 19.2) / 2 = **18.85m**
- You assign 18.85m to sprinters A and B

**CATASTROPHIC CONSEQUENCE:**
- In the PCA, the sprinters appear as **good throwers**
- The correlation circle will show that speed and throwing are **positively correlated**
- **THIS IS FALSE** - in reality, sprinters tend to be worse throwers

> **The problem:** The data is NOT missing at random (MCAR). It is missing because the sprinters **were injured in the throwing event** (probably due to lack of technique). This is a case of **MAR or MNAR**.

### 2.4. How to Diagnose the Type of Missing Data

Before imputing, perform these **diagnostic tests**:

#### Test 1: Visual Missingness Pattern

```python
import missingno as msno
import matplotlib.pyplot as plt

# Visualize missing data pattern
msno.matrix(df)
plt.show()

# Visualize correlation between missing data
msno.heatmap(df)
plt.show()
```

**Interpretation:**
- If the gaps are **randomly dispersed**: probably MCAR
- If the gaps **cluster in specific rows/columns**: probably MAR or MNAR

#### Test 2: Little's Test (MCAR Test)

```python
# Install: pip install pyampute
from pyampute.exploration import mcar_test

# Statistical test for MCAR
result = mcar_test(df)
print(f"p-value: {result}")
# If p > 0.05: MCAR not rejected (data MAY be random)
# If p < 0.05: MCAR rejected (data is NOT random)
```

#### Test 3: Compare Groups (Complete vs Incomplete Data)

```python
# Create missing data indicator
df['has_na'] = df['throwing'].isna()

# Compare means of other variables
print(df.groupby('has_na')['100m'].mean())
print(df.groupby('has_na')['long_jump'].mean())

# If means are VERY different, the data is NOT MCAR
```

### 2.5. Imputation Strategies by Type

| Missingness Type | Recommended Strategy | Strategy to AVOID |
|------------------|----------------------|-------------------|
| **MCAR** (purely random) | Mean, median, KNN, MICE | - |
| **MAR** (depends on other variables) | KNN, MICE, Multiple regression | Simple mean (biases) |
| **MNAR** (depends on the missing value) | Specific models, Sensitivity analysis | Mean, KNN, MICE (all bias) |

### 2.6. Alternatives to the Mean (Python Code)

#### Option 1: Drop Rows with NA (only if few and MCAR)

```python
# Only if you have FEW missing data (<5%) and they are MCAR
df_clean = df.dropna()
print(f"Rows removed: {len(df) - len(df_clean)}")
```

#### Option 2: KNN Imputation (respects local structure)

```python
from sklearn.impute import KNNImputer

# KNN finds the K most similar neighbors and averages their values
imputer = KNNImputer(n_neighbors=5)
df_imputed = pd.DataFrame(
    imputer.fit_transform(df[numeric_columns]),
    columns=numeric_columns
)
```

**Advantage:** A sprinter with NA in throwing will receive the value from **other similar sprinters**, not the global average.

#### Option 3: Multiple Imputation (MICE) - The Gold Standard

```python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# MICE: Multiple Imputation by Chained Equations
imputer = IterativeImputer(max_iter=10, random_state=42)
df_imputed = pd.DataFrame(
    imputer.fit_transform(df[numeric_columns]),
    columns=numeric_columns
)
```

**Advantage:** Uses ALL variables to predict the missing value through iterative regressions.

#### Option 4: Group-Based Imputation (when categories exist)

```python
# If you know the data depends on a category
df['throwing'] = df.groupby('athlete_type')['throwing'].transform(
    lambda x: x.fillna(x.mean())
)
```

**Example:** Impute a sprinter's throwing with the **mean of other sprinters**, not the global mean.

### 2.7. Checklist BEFORE Performing PCA

Before running your PCA analysis, verify:

- [ ] **How many NAs do I have?** `df.isna().sum()` - If > 20% in a variable, consider removing it
- [ ] **Where are the NAs?** `msno.matrix(df)` - Look for patterns
- [ ] **Are they random?** Little's test or group comparison
- [ ] **Which method should I use?**
  - MCAR + few NAs: Mean or drop rows
  - MAR: KNN or MICE
  - MNAR: Consult with a domain expert or sensitivity analysis

### 2.8. Practical Example: What to Do in the Decathlon

```python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# Load data
df = pd.read_csv('decathlon.csv')

# 1. Diagnosis
print("Missing data by column:")
print(df.isna().sum())

# 2. If there are NAs, check pattern
if df.isna().any().any():
    # Compare athletes with/without NAs
    df['has_na'] = df.isna().any(axis=1)
    print("\nMean comparison (with NA vs without NA):")
    print(df.groupby('has_na')[['100m', 'Long.jump']].mean())

    # If means are similar, probably MCAR -> we can impute
    # If means are very different, be careful -> use KNN or MICE

    # 3. Impute with KNN (respects structure)
    imputer = KNNImputer(n_neighbors=3)
    active_columns = ['100m', 'Long.jump', 'Shot.put', 'High.jump',
                        '400m', '110m.hurdle', 'Discus', 'Pole.vault',
                        'Javeline', '1500m']

    df[active_columns] = imputer.fit_transform(df[active_columns])
    print("\nImputation completed with KNN")

# 4. Now we CAN perform PCA
from prince import PCA
pca = PCA(n_components=5, rescale_with_std=True)
pca.fit(df[active_columns])
```

### 2.9. Summary: The 3-Step Rule

```
STEP 1: DIAGNOSE
   "Why is this data missing?"
   -> MCAR, MAR, or MNAR?

STEP 2: DECIDE
   "Can I impute without biasing?"
   -> If MNAR: DO NOT impute with mean
   -> If MAR: Use KNN or MICE
   -> If MCAR: Mean is acceptable

STEP 3: DOCUMENT
   "What did I do and why?"
   -> Report the % of NAs
   -> Report the method used
   -> Report whether results change
```

> **MORAL:** Plugging in the mean "just because" is like filling a hole in a puzzle with a piece from another puzzle. It might fit, but **the final picture will be distorted**.

---

## 2.10. FUNDAMENTAL: Why 0 is Valid and You Should NOT Always Impute

### 2.10.1. The Core Problem: Confusing "Complete Database" with "Correct Database"

One of the most serious conceptual errors made by students (and many professionals) is thinking that:

> **FALSE:** "A database must be complete to be analyzed"

This belief comes from programming (where `NULL` causes errors) and from machine learning (where many algorithms don't accept `NaN`). But in **real data analysis**, especially in surveys and Big Data, **missing data IS INFORMATION**, not a problem to "fix".

#### The Uncomfortable Truth:

| Wrong Belief | Reality |
|--------------|---------|
| "I must fill all NAs" | **NO**. You must understand WHY they are missing |
| "A complete database is better" | **NO**. A database with incorrect imputations is WORSE than one with NAs |
| "0 means no data" | **IT DEPENDS**. In surveys, 0 can be a valid response |
| "NaN and 0 are the same" | **FALSE**. They are conceptually different |

---

### 2.10.2. The Fundamental Difference: 0 vs NaN vs "No Response"

Imagine a survey about income and expenses:

| Question | Person A's Response | Person B's Response | Person C's Response |
|----------|-------------------|-------------------|-------------------|
| "How many cigarettes do you smoke per day?" | **0** (doesn't smoke) | **NaN** (refused to answer) | **20** (smokes 20) |
| "How much did you spend on tobacco this month?" | **0** (consistent: doesn't smoke) | **NaN** (didn't respond) | **150** (consistent: smokes) |

#### Analysis of Each Case:

**Person A - The 0 is VALID:**
- `cigarettes = 0` means **"DOES NOT SMOKE"**, it is a real response
- `tobacco_expense = 0` is **consistent** with not smoking
- **IMPUTING** these 0s with the mean would be **CATASTROPHIC**: you would turn a non-smoker into an average smoker

**Person B - The NaN is INFORMATIVE:**
- `cigarettes = NaN` means **"REFUSED TO ANSWER"**
- It could be because:
  - Smokes illegally (underage)
  - Embarrassed to admit smoking heavily
  - Simply doesn't want to share that information
- **IMPUTING** with the mean assumes they are an average smoker, which may be **FALSE**

**Person C - Complete Data:**
- Answered everything, no ambiguity

---

### 2.10.3. Sampling Concepts: Why Missing Data is Part of the Design

#### The Survey Context

When working with surveys or Big Data databases, **missing data is a natural consequence of the collection process**. According to sampling theory (see [TodoEconometria - Sampling Strategies](https://todoeconometria.com/estrategias-de-muestreo/)):

> **Simple Random Sampling:** The selection of a representative sample is highly complex. For example, if we want to study people with type 2 diabetes, **not everyone will answer every question**, and that is **expected and valid**.

#### The Three Real Scenarios:

**Scenario 1: Control Questions (Filters)**

In well-designed surveys, there are questions that **intentionally** generate `NaN` in other variables:

```
Q1: "Do you own a car?"
    [ ] Yes  -> Go to Q2
    [ ] No   -> Skip to Q5

Q2: "What brand is your car?" (Only if answered Yes in Q1)
    _____________
```

**Result in the database:**

| Person | Has_Car | Car_Brand |
|--------|---------|-----------|
| John | Yes | Toyota |
| Mary | **No** | **NaN** |

**Question:** Should we impute Mary's car brand?

**Answer:** **NO**. The `NaN` is **correct**. Mary doesn't have a car, therefore **she cannot have a brand**. Imputing "Toyota" (the mean/mode) would be absurd.

---

**Scenario 2: Non-Response Due to Sensitivity**

Some questions are sensitive:

```
Q10: "What is your monthly income?"
     [ ] Less than $1000
     [ ] $1000 - $3000
     [ ] $3000 - $5000
     [ ] More than $5000
     [ ] Prefer not to answer
```

**Result:**

| Person | Income |
|--------|--------|
| Peter | $1000-$3000 |
| Ana | **NaN** (prefers not to answer) |

**Question:** Should we impute Ana's income with the median?

**Answer:** **IT DEPENDS on the missingness type:**
- If Ana is **wealthy** and doesn't want to disclose it: **MNAR** (data is missing because it's high)
- If Ana randomly chose "prefer not to answer": **MCAR** (random)

**Imputing with the median in the MNAR case** will introduce **downward bias** (we assume that the wealthy who don't respond have average income).

---

**Scenario 3: Big Data with Sensors**

In IoT databases, sensors, or logs:

```
Temperature Sensor:
Time  | Temperature
------|------------
10:00 | 25.3°C
10:05 | 25.5°C
10:10 | NaN  (sensor failed)
10:15 | 26.1°C
```

**Question:** Should we impute 10:10 with the mean of 10:05 and 10:15?

**Answer:** **IT DEPENDS:**
- If the sensor fails **randomly**: MCAR -> Linear imputation is reasonable
- If the sensor fails **when it's very hot** (overheats): MNAR -> Imputing with the mean will **underestimate** the actual temperature

---

### 2.10.4. The Conceptual Error: "I Need Complete Data to Analyze"

#### Myth 1: "Algorithms don't accept NaN"

**Reality:**
- Many algorithms **DO** accept NaN: decision trees, Random Forest, XGBoost
- Those that don't accept NaN (linear regression, classic PCA) have **robust versions**:
  - PCA with `prince` accepts NA
  - Regression with `statsmodels` has `missing='drop'`

#### Myth 2: "More data = Better model"

**Reality:**
- **Incorrect data** (poorly imputed) are **worse** than **fewer correct data**
- Example:

```python
# Option A: Impute with mean (BAD if MNAR)
df['income'].fillna(df['income'].mean())  # 1000 rows, but with bias

# Option B: Drop rows with NA (GOOD if few)
df.dropna(subset=['income'])  # 800 rows, but without bias
```

**Which is better?** It depends on the % of NAs:
- If NA < 5%: **Dropping** is safe
- If NA > 20%: **Investigate** why they are missing before deciding

---

### 2.10.5. Practical Case: Consumer Habits Survey

Imagine this database:

| Person | Smokes | Cigarettes_Day | Tobacco_Expense | Drinks_Alcohol | Drinks_Week |
|--------|--------|----------------|-----------------|----------------|-------------|
| A | No | **0** | **0** | Yes | 3 |
| B | Yes | 10 | 50 | No | **0** |
| C | Yes | **NaN** | **NaN** | Yes | **NaN** |
| D | No | **0** | **0** | No | **0** |

#### Correct Analysis:

**Person A:**
- `Cigarettes_Day = 0` is **VALID** (doesn't smoke)
- `Tobacco_Expense = 0` is **VALID** (consistent)
- **DO NOT IMPUTE**

**Person B:**
- `Drinks_Week = 0` is **VALID** (doesn't drink)
- **DO NOT IMPUTE**

**Person C:**
- `Cigarettes_Day = NaN` is **PROBLEMATIC**
- Options:
  1. **Drop row** (if it's the only one with NA)
  2. **Impute with KNN** (find similar smokers)
  3. **Leave as NA** and use algorithms that support it

#### INCORRECT Analysis (Common Among Beginners):

```python
# ERROR: Impute EVERYTHING with the mean
df.fillna(df.mean())
```

**Consequence:**
- Person A (non-smoker) now has `Cigarettes_Day = 5` (mean of B and C)
- Person D (non-smoker, non-drinker) now smokes and drinks
- **The database is DESTROYED**

---

### 2.10.6. Golden Rules for Students

#### Rule 1: Before Touching an NA, Ask Yourself:

```
1. Why is this data missing?
   - Filter question? -> NA is CORRECT, DO NOT impute
   - Non-response? -> Investigate type (MCAR/MAR/MNAR)
   - Technical error? -> Could be MCAR

2. Is it a 0 or a NaN?
   - 0 = Valid response ("I don't have", "I don't do")
   - NaN = Absence of response

3. What happens if I impute incorrectly?
   - Bias in results
   - Erroneous conclusions
   - Invalid model
```

#### Rule 2: Decision Workflow

```
STEP 1: Count NAs
   df.isna().sum()
   -> If < 5%: Consider dropping rows
   -> If > 20%: Investigate pattern

STEP 2: Visualize pattern
   import missingno as msno
   msno.matrix(df)
   -> Random? -> MCAR
   -> Clustered? -> MAR/MNAR

STEP 3: Statistical test
   from pyampute.exploration import mcar_test
   mcar_test(df)
   -> p > 0.05: MCAR (you can impute)
   -> p < 0.05: MAR/MNAR (be careful)

STEP 4: Decide strategy
   - MCAR + few NAs: Mean or drop
   - MAR: KNN or MICE
   - MNAR: DO NOT impute or use specific model
   - Filter question: LEAVE as NA
```

#### Rule 3: ALWAYS Document

```python
# GOOD PRACTICE
print("="*50)
print("MISSING DATA REPORT")
print("="*50)
print(f"Total observations: {len(df)}")
print(f"Variables with NA: {df.isna().any().sum()}")
print(f"\nDetail by variable:")
print(df.isna().sum())
print(f"\nPercentage of NAs:")
print((df.isna().sum() / len(df) * 100).round(2))
print("\nStrategy applied:")
print("- Variables with valid 0: ['Cigarettes_Day', 'Drinks_Week']")
print("- Variables imputed with KNN: ['Income']")
print("- Rows removed: 3 (0.5% of total)")
```

---

### 2.10.7. Full Example: Correct vs Incorrect Code

#### INCORRECT Code (Beginner):

```python
import pandas as pd

# Load data
df = pd.read_csv('survey.csv')

# ERROR: Impute EVERYTHING with the mean
df = df.fillna(df.mean())

# ERROR: Don't verify what happened
print("Done, complete database!")
```

**Problems:**
1. Doesn't distinguish between valid 0 and NaN
2. Doesn't verify missingness type
3. Doesn't document what was done
4. May have destroyed the real structure

#### CORRECT Code (Professional):

```python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
import missingno as msno
import matplotlib.pyplot as plt

# 1. Load and explore
df = pd.read_csv('survey.csv')
print("INITIAL DIAGNOSIS")
print("="*50)
print(df.info())
print("\nMissing data:")
print(df.isna().sum())

# 2. Visualize pattern
msno.matrix(df)
plt.title("Missing Data Pattern")
plt.show()

# 3. Separate variables with valid 0 from variables with NA
# Variables where 0 is valid (do not impute)
vars_with_valid_zero = ['Cigarettes_Day', 'Tobacco_Expense', 'Drinks_Week']

# Variables where NA must be treated
vars_to_impute = ['Income', 'Age', 'Work_Hours']

# 4. Verify consistency (0 in dependent variables)
# Example: If doesn't smoke, tobacco expense must be 0
mask_non_smoker = df['Smokes'] == 'No'
assert (df.loc[mask_non_smoker, 'Cigarettes_Day'] == 0).all(), \
    "ERROR: There are non-smokers with cigarettes > 0"

# 5. Impute only numeric variables that need it
if df[vars_to_impute].isna().any().any():
    print("\nApplying KNN Imputer to:", vars_to_impute)
    imputer = KNNImputer(n_neighbors=5)
    df[vars_to_impute] = imputer.fit_transform(df[vars_to_impute])
    print("Imputation completed")

# 6. Document
print("\n" + "="*50)
print("FINAL REPORT")
print("="*50)
print(f"Total rows: {len(df)}")
print(f"Variables with valid 0 (NOT imputed): {vars_with_valid_zero}")
print(f"Variables imputed with KNN: {vars_to_impute}")
print(f"Remaining NAs: {df.isna().sum().sum()}")
```

---

### 2.10.8. Summary: The Data Analyst's Philosophy

> **"It's not your job to fill gaps. It's your job to UNDERSTAND why there are gaps."**

#### Fundamental Principles:

1. **Missing data is information**, not an error
2. **0 is a valid response**, not missing data
3. **NaN means "unknown"**, and sometimes **"unknown" is the correct answer**
4. **Imputing incorrectly is worse than not imputing**
5. **Document EVERYTHING** you do with NAs

#### Final Checklist Before Performing PCA (or Any Analysis):

- [ ] Have I identified all variables with valid 0?
- [ ] Have I verified that the 0s are consistent with other variables?
- [ ] Have I diagnosed the missingness type (MCAR/MAR/MNAR)?
- [ ] Have I decided on a justified strategy for each variable?
- [ ] Have I documented how many NAs there were and what I did with them?
- [ ] Have I verified that the results make sense after imputation?

---

## 3. The Dataset: Decathlon - Context and Research Questions

### 3.1. The Real Scenario: What Problem Are We Trying to Solve?

Imagine you are the **technical director of an athletics federation**. You have data from 41 athletes who competed in the decathlon (10 events) in two different competitions: the **Olympic Games** and the **Decastar Meeting**.

You face several **business/research questions**:

| Question | Why it matters |
|----------|---------------|
| Are there athlete "profiles"? (sprinters vs throwers vs all-rounders) | To design specialized training programs |
| Which events are related to each other? | To optimize cross-training |
| Do Olympic athletes have a different profile than Decastar athletes? | To understand what characterizes elite athletes |
| Which events are "redundant" (measure the same thing)? | To simplify evaluations |
| Which athletes have atypical profiles? | To identify unique talents or detect anomalies |

> **KEY:** We don't apply PCA "just because" or "because it's trendy". We apply it because we have **specific questions** that this technique can answer **efficiently and validly**.

### 3.2. Why PCA is the Right Tool (and Not Another)

#### The Mathematical Problem

We have **10 numerical variables** (the events). Visualizing 10 dimensions is impossible. But:

- We don't want to lose important information
- We want to see **patterns** (groups of athletes, relationships between events)
- We want to **reduce complexity** without destroying the structure

#### Why NOT Other Techniques?

| Technique | Why it is NOT suitable here |
|-----------|----------------------------|
| **Regression** | We don't have a "target" variable to predict. We want to explore, not predict. |
| **Clustering (K-Means)** | Groups individuals but doesn't explain WHICH variables differentiate them or how variables relate to each other. |
| **Simple Correlation** | Only compares variables 2 at a time. With 10 variables, we'd have 45 correlations. Impossible to interpret. |
| **t-SNE / UMAP** | Good for visualization but don't provide interpretation of the dimensions (they are "black boxes"). |

#### Why USE PCA?

| PCA Advantage | Application in Decathlon |
|---------------|------------------------|
| **Reduces dimensions** preserving variance | From 10 events to 2-3 interpretable dimensions |
| **Identifies which variables "go together"** | Discover that 100m, long jump, and 400m are correlated |
| **Detects atypical individuals** | Identify athletes with unique profiles |
| **Allows supplementary variables** | See if "Competition" explains differences without contaminating the analysis |
| **Is interpretable** | Each axis has a meaning (e.g., "speed vs endurance") |

### 3.3. The Sporting Context of the Decathlon

The decathlon is known as **"the king of athletics events"** because it evaluates the most complete athlete. It consists of 10 events over 2 days:

#### Day 1

| Event | Type | Primary Skill |
|-------|------|---------------|
| 100m | Race | Explosive speed |
| Long jump | Jump | Leg power |
| Shot put | Throw | Brute strength |
| High jump | Jump | Technique + power |
| 400m | Race | Speed-endurance |

#### Day 2

| Event | Type | Primary Skill |
|-------|------|---------------|
| 110m hurdles | Race | Speed + technique |
| Discus throw | Throw | Strength + technique |
| Pole vault | Jump | Advanced technique |
| Javelin throw | Throw | Strength + coordination |
| 1500m | Race | Pure endurance |

> **Prior hypothesis (before PCA):** We expect to find that events group by "skill type": speed (100m, 400m, hurdles), strength (shot put, discus, javelin), and technique (pole vault, high jump). PCA will tell us whether this hypothesis is correct.

### 3.4. The Two Competitions: Why Does It Matter?

| Competition | Level | Characteristics |
|-------------|-------|-----------------|
| **Olympic Games** | World elite | Only the best in the world. High pressure. Maximum preparation. |
| **Decastar Meeting** | High European level | Elite competitors, but not necessarily the best in the world. |

**Key question:** Do Olympic athletes have a **different performance profile**? Or are they simply "better at everything"?

- If they are "better at everything", they will be in the same direction as Decastar athletes but farther from the origin.
- If they have a **different profile**, they will be in a different zone of the map.

This question is answered by using `Competition` as a **supplementary variable**: it doesn't participate in the PCA calculation, but we project it to see if the groups separate.

### 3.5. Data Structure

| Variable Type | Variables | Role in the Analysis |
|---------------|-----------|---------------------|
| **Active** | 100m, Long.jump, Shot.put, High.jump, 400m, 110m.hurdle, Discus, Pole.vault, Javeline, 1500m | **Build the PCA axes** |
| **Quantitative Supplementary** | Rank, Points | Projected but do **NOT** build axes |
| **Qualitative Supplementary** | Competition (Decastar/OlympicG) | For **coloring and segmenting** |

### 3.6. Key Concept: Active vs. Supplementary Variables

This is one of the most powerful concepts in FactoMineR:

> **Active Variables:** Participate in the mathematical calculation of principal components. They are the ones that "build" the axes. In our case, the 10 sporting events.
>
> **Supplementary Variables:** Do **NOT** participate in the calculation, but are projected onto the factorial space to see how they relate to the found dimensions.

**Why is it useful?** Imagine you want to know whether the type of competition (Olympic Games vs Decastar) influences the athletes' performance profile. If you include "Competition" as an active variable, you **contaminate** the analysis (you introduce a categorical variable in a numerical calculation). But if you use it as a **supplementary** variable, you can see if the groups separate **without having forced that separation**.

### 3.7. Other Classic PCA Datasets and Their Contexts

So you understand that PCA is applied in **many domains**, here are other classic datasets:

| Dataset | Context | Research Question | Variables |
|---------|---------|-------------------|-----------|
| **Iris** (Fisher, 1936) | Botany | Can petal/sepal measurements distinguish flower species? | 4 flower measurements, 3 species |
| **Wine** (UCI) | Oenology | What chemical properties characterize wines from different regions? | 13 chemical properties, 3 origins |
| **Breast Cancer** (UCI) | Medicine | What cell measurements distinguish benign from malignant tumors? | 30 cell nucleus measurements |
| **MNIST** (LeCun) | Computer vision | Can 784-pixel images be reduced to few dimensions? | 784 pixels, 10 digits |
| **Social surveys** | Sociology | What latent dimensions explain political opinions? | Many survey questions |

> **Common pattern:** In all cases, we have **many numerical variables** and want to **discover latent structure** (hidden dimensions that explain the variation).

### 3.8. Checklist: Before Applying PCA, Ask Yourself...

- [ ] **Do I have a clear question?** "I want to explore patterns" is valid. "I want to predict Y" is not for PCA.
- [ ] **Are my variables numerical?** PCA requires quantitative variables (or convertible to numerical).
- [ ] **Do I have enough observations?** Rule of thumb: at least 5-10 observations per variable.
- [ ] **Are the variables on comparable scales?** If not, I must standardize (Prince does this by default).
- [ ] **Have I handled missing data?** (See section 2)
- [ ] **Do I have supplementary variables to validate?** Very useful for interpreting results.

---

## 4. Analysis Results: Chart Panel

Below is the complete chart panel generated by the `02_PCA_FactoMineR_style.py` script:

![PCA Chart Panel](02_PCA_FactoMineR_graficos.png)

---

## 5. Detailed Interpretation of Each Chart

### 4.1. SCREE PLOT

**Location:** Upper left panel

**What it shows:** The variance explained by each principal component.

![Scree Plot Interpretation](02_PCA_FactoMineR_graficos.png)

#### Reading the Results:

| Dimension | Explained Variance | Cumulative Variance |
|-----------|-------------------|---------------------|
| Dim.1 | 16.7% | 16.7% |
| Dim.2 | 14.5% | 31.2% |
| Dim.3 | 12.8% | 44.0% |
| Dim.4 | 11.9% | 55.9% |
| Dim.5 | 9.6% | 65.5% |

#### Interpretation:

1. **The gray dashed line (Threshold = 10%)** represents the expected contribution if all variables were independent (100% / 10 variables = 10%). Dimensions **above** this line contribute more information than the average.

2. **The first 4 dimensions** have eigenvalues greater than 1 (Kaiser Rule), suggesting retaining 4 components.

3. **The red curve (cumulative)** shows that with 5 dimensions we capture 65.5% of the total variability. This is relatively low, indicating that **the decathlon is a multidimensional sport** where no single "factor" explains all performance.

> **Sporting Insight:** Unlike sports such as swimming (where speed explains almost everything), the decathlon requires **multiple independent skills**: speed, strength, endurance, technique. That's why no dimension clearly dominates.

---

### 4.2. CORRELATION CIRCLE (The Most Important Chart)

**Location:** Upper center panel

This is **the most important chart in FactoMineR**. It shows how variables relate to each other and to the axes.

![Correlation Circle](02_PCA_circulo_correlacion.png)

#### How to Read the Circle:

| Situation in the Chart | Meaning |
|------------------------|---------|
| Arrow **near the circle** (edge) | Variable **well represented** in the plane |
| **Short** arrow (near the center) | Variable **poorly represented**, its variance is in other dimensions |
| Arrows in the **same direction** | Variables **positively correlated** |
| **Opposite** arrows (180 degrees) | Variables **negatively correlated** |
| **Perpendicular** arrows (90 degrees) | Variables **not correlated** |

#### Interpretation of Our Results:

**Group 1 - Lower Left Quadrant (Speed/Agility):**
- `Long.jump` (long jump): Long arrow to the left
- `400m`: Similar direction
- `110m.hurdle`: Similar direction

> **Interpretation:** These events are **positively correlated with each other**. An athlete good at long jump tends to be good at 400m and hurdles. This makes sense: they all require **explosive speed and leg power**.

**Group 2 - Upper Left Quadrant (Endurance):**
- `1500m`: Arrow toward upper-left
- `Shot.put` (shot put): Upward

> **Interpretation:** The 1500m (endurance) and shot put appear in different directions from the speed group. This suggests that **endurance is a distinct skill** from explosive speed.

**Group 3 - Lower Right Quadrant:**
- `Pole.vault` (pole vault): Long arrow downward
- `Discus`: Similar direction

> **Interpretation:** These technical events form their own group.

**Special Variable - `Long.jump`:**
- It is the **longest** arrow toward the left
- Correlation with Dim.1: **-0.74** (very high)

> **Conclusion:** Long jump is the variable that **best defines** the first dimension. An athlete with a high score on Dim.1 (right side of the map) tends to have a **worse** long jump.

---

### 4.3. INDIVIDUAL MAP

**Location:** Upper right panel

Shows where each athlete is located in the space of the first two dimensions, colored by the supplementary variable `Competition`.

#### Reading the Chart:

- **Blue points:** Athletes from the **Decastar** competition
- **Red points:** Athletes from the **Olympic Games (OlympicG)**

#### Interpretation:

1. **General spread:** Athletes are widely distributed across the plane, without forming very compact groups. This confirms that **there is diversity of profiles** in the decathlon.

2. **Separation by competition:** Observe that red points (Olympic) tend to be more dispersed and some are in extreme positions (e.g., BERNARD at the far right). Olympic athletes show **greater variability** in their profiles.

3. **Notable athletes:**
   - **BERNARD** (far right): Very distinctive profile, different from the average
   - **Zsivoczky** (below): Another atypical profile
   - **BOURGUIGNON** (upper left): Different profile

4. **Combined interpretation with the circle:**
   - Athletes on the **left** of the map tend to be good at `Long.jump`, `400m`, `110m.hurdle` (speed events)
   - Athletes **above** tend to be good at `Shot.put`, `1500m` (strength/endurance)

---

### 4.4. VARIABLE CONTRIBUTIONS TO DIM.1

**Location:** Lower left panel

This chart answers the question: **Which variables "built" the first axis?**

#### Results:

| Variable | Contribution to Dim.1 |
|----------|----------------------|
| **Long.jump** | **32.9%** |
| **1500m** | **19.9%** |
| **400m** | **12.0%** |
| **110m.hurdle** | **10.8%** |
| High.jump | 7.6% |
| Javeline | 6.6% |
| Shot.put | 5.0% |
| 100m | 4.0% |
| Pole.vault | 1.1% |
| Discus | 0.1% |

#### Interpretation:

- The **dashed red line** marks the expected contribution threshold (10% = 100%/10 variables)
- The **red** bars (above threshold) are the variables that **truly define** that dimension
- The **blue** bars (below threshold) contribute less than expected

> **Conclusion for Dim.1:** This dimension is dominated by `Long.jump` (32.9%), followed by `1500m` (19.9%) and `400m` (12.0%). This suggests that Dim.1 represents a **continuum between explosive athletes (good at long jump, 400m) vs endurance athletes (1500m)**.

---

### 4.5. VARIABLE CONTRIBUTIONS TO DIM.2

**Location:** Lower center panel

#### Results:

| Variable | Contribution to Dim.2 |
|----------|----------------------|
| **Shot.put** | **34.1%** |
| **Pole.vault** | **30.7%** |
| **1500m** | **10.6%** |
| **High.jump** | **10.1%** |
| Javeline | 8.7% |
| Discus | 3.0% |
| Long.jump | 1.2% |
| 100m | 0.9% |
| 400m | 0.7% |
| 110m.hurdle | 0.2% |

#### Interpretation:

> **Conclusion for Dim.2:** This dimension is dominated by `Shot.put` (34.1%) and `Pole.vault` (30.7%). It represents a **contrast between throwing athletes (brute strength) vs technical athletes (pole vault)**.

**Important note:** Observe that `Shot.put` and `Pole.vault` point in **opposite directions** in the correlation circle. This means:
- Athletes **above** on the map: Good at shot put
- Athletes **below** on the map: Good at pole vault

---

### 4.6. BIPLOT (Individuals + Variables)

**Location:** Lower right panel

The biplot **combines** the individual map with variable arrows, allowing you to directly see which variables characterize which athletes.

#### How to Read It:

1. **Mentally project** each athlete onto each variable arrow
2. If the projection falls in the **direction of the arrow**: the athlete has a **high** value in that variable
3. If the projection falls in the **opposite direction**: the athlete has a **low** value in that variable

#### Interpretation Example:

- **BERNARD** (far right):
  - Projection onto `Long.jump` (left): **opposite** = poor long jump
  - Projection onto `Shot.put` (up): **perpendicular** = average

- **Athletes upper-left**:
  - Good at `1500m` and `Shot.put`
  - **Endurance and strength** profile

---

## 6. Advanced FactoMineR Metrics

### 5.1. Quality of Representation ($\cos^2$)

The $\cos^2$ measures **how well represented** a point is in the factorial plane.

$$\cos^2 = \frac{\text{distance to origin in the plane}^2}{\text{distance to origin in the original space}^2}$$

#### Interpretation:

| $\cos^2$ Value | Meaning |
|----------------|---------|
| Close to **1** | The point is **perfectly represented** in the plane |
| Close to **0** | The point is **poorly represented**, its information is in other dimensions |

#### Results for Athletes (Top 5 Best Represented):

| Athlete | $\cos^2$ in Dim1+Dim2 | Interpretation |
|---------|----------------------|----------------|
| Bourguignon | 0.755 | 75.5% of its variability captured |
| BERNARD | 0.725 | 72.5% of its variability captured |
| Warners | 0.717 | 71.7% of its variability captured |
| Lorenzo | 0.679 | 67.9% of its variability captured |
| Clay | 0.638 | 63.8% of its variability captured |

> **Practical application:** If you are going to interpret a specific athlete's position, **first check their $\cos^2$**. If it is low (< 0.5), their position on the map may be misleading.

---

### 5.2. Contributions

Contributions indicate **how much** each individual/variable contributes to the construction of an axis.

#### For Variables:

We already saw that `Long.jump` contributes 32.9% to Dim.1. This means that if we removed long jump from the analysis, **the first dimension would change drastically**.

#### For Individuals:

| Athlete | Contribution to Dim.1 |
|---------|----------------------|
| BERNARD | 12.82% |
| Warners | 12.42% |
| Clay | 8.62% |

> **Interpretation:** BERNARD and Warners are "influential" athletes who "pull" the axis toward their positions. They are athletes with extreme profiles.

---

## 7. R/Python Equivalence Table

For those coming from R who want to replicate FactoMineR analyses:

| FactoMineR (R) | Prince (Python) | Description |
|----------------|-----------------|-------------|
| `res.pca$eig` | `pca.eigenvalues_summary` | Eigenvalue table |
| `res.pca$ind$coord` | `pca.row_coordinates(df)` | Individual coordinates |
| `res.pca$ind$contrib` | `pca.row_contributions_` | Individual contributions |
| `res.pca$ind$cos2` | `pca.row_cosine_similarities(df)` | Individual cos2 |
| `res.pca$var$coord` | `pca.column_coordinates` | Variable coordinates |
| `res.pca$var$cor` | `pca.column_correlations` | Variable correlations |
| `res.pca$var$contrib` | `pca.column_contributions_` | Variable contributions |
| `res.pca$var$cos2` | `pca.column_cosine_similarities_` | Variable cos2 |

---

## 8. Decathlon Analysis Conclusions

### 7.1. Main Findings

1. **The decathlon is multidimensional:** No dimension explains more than 17% of the variance. At least 4 components are needed to capture 56% of the information.

2. **Dimension 1 - Speed/Agility vs Endurance:**
   - Dominated by: `Long.jump` (32.9%), `1500m` (19.9%), `400m` (12.0%)
   - Separates explosive athletes from endurance athletes

3. **Dimension 2 - Strength vs Technique:**
   - Dominated by: `Shot.put` (34.1%), `Pole.vault` (30.7%)
   - Separates throwing athletes from technical athletes

4. **Supplementary variable (Competition):**
   - Olympic athletes show greater variability in their profiles
   - There is no clear separation between competitions, suggesting that **the level of competition does not determine the profile type**

### 7.2. Practical Implications

- **For coaches:** Identifying which quadrant an athlete falls in helps design personalized training programs
- **For analysts:** Contributions reveal which variables are most important for characterizing overall performance

---

## 9. Generated Files

| File | Description |
|------|-------------|
| `02_PCA_FactoMineR_style.py` | Complete Python code |
| `02_PCA_FactoMineR_style.md` | This manual |
| `02_PCA_FactoMineR_graficos.png` | Panel of 6 charts |
| `02_PCA_circulo_correlacion.png` | Individual correlation circle |
| `02_PCA_resultados_FactoMineR.xlsx` | Excel with 7 result sheets |

---

## 10. Proposed Exercise for the Student

### Comprehension Questions:

1. **If an athlete has a negative coordinate on Dim.1, what can you infer about their long jump?**

2. **Why does `Discus` have an almost null contribution (0.1%) to Dim.1?**

3. **If an athlete's $\cos^2$ in the Dim1-Dim2 plane is 0.30, should we trust their position on the map? Why?**

4. **Looking at the biplot, what type of profile does athlete YURKOV (above on the map) have?**

### Answers:

1. They have a good long jump (Long.jump's correlation with Dim.1 is negative: -0.74)

2. Because Discus variability is mainly represented in Dim.3 (contribution 39.4%), not in Dim.1

3. We should not trust it much. Only 30% of their variability is captured in that plane. The remaining 70% is in other dimensions.

4. YURKOV has high values in the variables that point upward (`Shot.put`, `1500m`, `High.jump`): a strength and endurance profile.

---

## 11. Academic References

### Main Tutorial Reference

> **FactoMineR Tutorial**
> Husson, F., & Josse, J.
> [http://factominer.free.fr/course/FactoTuto.html](http://factominer.free.fr/course/FactoTuto.html)
> *"This course presents the main methods used in Exploratory Data Analysis with the FactoMineR package."*

### Original FactoMineR Article

> Le, S., Josse, J., & Husson, F. (2008).
> **FactoMineR: An R Package for Multivariate Analysis.**
> *Journal of Statistical Software*, 25(1), 1-18.
> DOI: 10.18637/jss.v025.i01

### Reference Book

> Husson, F., Le, S., & Pages, J. (2017).
> **Exploratory Multivariate Analysis by Example Using R.**
> 2nd Edition. CRC Press.
> ISBN: 978-1138196346

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​‌‌​​​​‌‍​​‌‌​‌​​‍​‌‌​​​​‌‍​‌‌​​​‌‌‍​​‌‌​​​​‍​‌‌​​‌‌​‍​‌‌​​​‌‌﻿---

## Institutional Information

**Author/Reference:** @TodoEconometria
**Professor:** Juan Marcelo Gutierrez Miranda
**Area:** Big Data, Data Science & Applied Econometrics.

**Certification Hash ID:**
`4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
