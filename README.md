# Hi there, I'm Natalie Mugoni 👋

---

## 🙋‍♀️ About Me

I am a university student passionate about the continuous cycle of learning and unlearning. I enjoy exploring how complex systems work , whether built with code, data, or logic. My academic journey is driven by curiosity and a commitment to mastering modern technology to solve real-world problems.

- 🎓 BSc Honours in Data Science & Systems — University of Zimbabwe
- 🌍 Based in Harare, Zimbabwe
- 🔍 Currently seeking an industrial attachment in Data Science / Data Analytics

---

## 🛠️ Skills & Tools

| Category | Tools |
|---|---|
| **Languages** | Python, SQL |
| **Libraries** | pandas, NumPy, scikit-learn, matplotlib, seaborn, TensorFlow |
| **BI & Visualisation** | Power BI |
| **Databases** | MySQL |
| **Other** | Google Colab, R, Google Forms, Flask |
| **Concepts** | Machine Learning, NLP, Probability Theory, ER Modelling, EDA |

---

## 📂 Featured Projects

---

### 🌿 Harare Wetland Environmental Analysis & Predictive Modelling

> Environmental data analysis and machine learning on Harare's combined wetlands dataset, sourced from **ZimGeoPortal**.

**Objective:** Understand and predict the sensitivity levels of Harare's wetlands to support conservation, environmental planning, and policy-making.

#### 🔬 What Was Done

**1. Exploratory Data Analysis (EDA)**
- Loaded and profiled the `Harare_Combined_Wetlands_Dataset.csv`
- Identified and handled missing values — `Wetland_Type` (23.93% missing) imputed with the mode (`Head Water`)
- Univariate and bivariate analysis using histograms, count plots, and correlation heatmaps
- Stacked bar chart showing **wetland sensitivity across the top 10 suburbs**

**2. K-Means Clustering**
- Features: `Wetland_Type`, `Sensitivity_Level`, `Has_Major_River`, `Has_Dam`, `Has_Health_Facility`, `Road_Density_Rating`
- Applied **One-Hot Encoding** and **StandardScaler** for preprocessing
- Used the **Elbow Method** to determine optimal clusters → **k = 3**
- Visualised clusters in 2D using **PCA (Principal Component Analysis)**

**3. Decision Tree Classification**
- Target: Predict `Sensitivity_Level` (Highly Sensitive / Moderately Sensitive / Non-Sensitive)
- 80/20 train-test split with stratification
- Achieved **79.17% accuracy** on the test set
- Perfect classification of all *Moderately Sensitive* wetlands
- Feature importance identified `Wetland_Type_Middle Reach` and `Has_Major_River` as top predictors

#### 📊 Model Results Summary

| Sensitivity Class | Recall |
|---|---|
| Highly Sensitive | 80% |
| Moderately Sensitive | 100% |
| Non-Sensitive | 50% |

#### 🧰 Tools & Libraries
`Python` · `pandas` · `NumPy` · `scikit-learn` · `matplotlib` · `seaborn` · `Google Colab`

#### 💡 Key Recommendations
- Prioritise conservation for **Highly Sensitive** wetlands, especially in high-risk suburbs
- Explore **green financing** (green bonds, conservation grants) for wetland protection
- Future work: incorporate GIS/spatial analysis, temporal trends, and advanced models (Random Forest, Gradient Boosting)

> 📁 Dataset Source: [ZimGeoPortal](https://www.zimgeoportal.gov.zw/)

---

### 🧠 Mental Health Awareness & Help-Seeking Behavior Survey

> A survey-based data analysis project exploring student mental health awareness at university level, cleaned in **R** and visualised in **Power BI**.

**Sample Size:** 64 valid responses | **Platform:** Google Forms

#### ❓ Research Questions
1. What is the relationship between students' **awareness of mental health resources** and their **willingness to seek help**?
2. How do **demographic factors** (gender, year of study, major) influence attitudes toward mental health?
3. What are the **primary barriers** preventing students from accessing mental health support?

#### 🔬 Methodology
- 7 Likert-scale questions + 3 open-ended questions + 6 demographic questions
- Data cleaned in **R** (duplicate removal, missing value handling, text standardisation)
- Visualised in **Power BI** with interactive slicers, clustered bar charts, heatmaps, and donut charts

#### 📊 Key Findings

| Metric | Value |
|---|---|
| Average Awareness Score | 3.2 / 5.0 |
| Students who sought professional help | 22% |
| Top barrier — Social stigma | 4.1 / 5.0 |
| Second barrier — Cost/affordability | 3.7 / 5.0 |

- **Female students** showed higher comfort seeking help (M = 3.5) vs. males (M = 2.8)
- Awareness rose with academic progression: 1st year (M = 2.4) → 4th year (M = 3.9)
- Heatmap insight: **1st year male students** had the lowest awareness (M = 2.1); **4th year female students** had the highest (M = 4.2)

#### 🧰 Tools
`R` · `Power BI` · `Google Forms`

#### 📁 Project Assets

| Resource | Link |
|---|---|
| 📝 Survey Form | [View](https://docs.google.com/forms/d/e/1FAIpQLSd-uVL-AhHuPaLvcb9MsZj1I4sQNZlTL70INhqsj1ibyEZHDg/viewform?usp=header) |
| 📂 Raw Data | [Google Drive](https://drive.google.com/file/d/1DIxcT_pZSvZ1ONq_oEmpx-oXCbEfvv5A/view?usp=drive_link) |
| 🧹 Cleaned Data | [Google Drive](https://drive.google.com/file/d/1Vxxy8yI2__DJS-wJGiKJqgpjX7-ofwxT/view?usp=drive_link) |
| 📊 Power BI Visuals | [Google Drive](https://drive.google.com/file/d/1ZKIMCdGb6M0ZtoOM3XuJrd-PvfqBlQJy/view?usp=drive_link) |

---

### 🤖 Harvard CS50 AI — 12 Projects

> Successfully completed twelve projects as part of **Harvard's CS50 Introduction to Artificial Intelligence with Python**, implementing foundational AI algorithms from scratch.

| Domain | Topics Covered |
|---|---|
| **Search** | Minimax for adversarial games, puzzle-solving search strategies |
| **Knowledge** | Propositional logic, inference engines, logical puzzle solving |
| **Uncertainty** | Bayesian Networks, Markov Models, probability prediction |
| **Optimization** | Constraint satisfaction, scheduling problems |
| **Learning** | Reinforcement Learning agents, Neural Networks with TensorFlow |
| **Language** | NLP — syntax parsing, information retrieval |

---

## 📜 Certifications

- 🏅 Harvard CS50 — Artificial Intelligence with Python
- 🏅 ICDL (International Computer Driving Licence)

---





