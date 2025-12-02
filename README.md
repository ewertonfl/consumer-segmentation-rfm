# 📌 **README.md**

# Consumer Profiling & Behavioral Clustering
**Author:** Ewerton Florencio  
**LinkedIn:** https://www.linkedin.com/in/ewertonfl/

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Project Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📘 Project Overview

This project performs **customer segmentation** using a combination of:

- RFM Analysis (Recency, Frequency, Monetary)
- Unsupervised Machine Learning (K-Means / DBSCAN)
- Data Cleaning & Feature Engineering
- Exploratory Data Analysis (EDA)
- Visualization of behavioral patterns

The objective is to build a **market-relevant**, **realistic**, and **fully reproducible** Data Science pipeline that demonstrates both **Data Engineering** and **Machine Learning** capabilities.

The dataset used is **public** and does **not** contain sensitive information.

**Dataset:** https://archive.ics.uci.edu/dataset/352/online+retail

---

## 🎯 Business Purpose

Companies often struggle to understand **which customer groups drive value** and how to personalize campaigns.

This project solves that by:

- Identifying customer behavior clusters  
- Providing actionable insights from RFM metrics  
- Creating segment-based recommendations  
- Building a clean and modular codebase suitable for production

---

## 🏗️ Architecture

The project follows a simplified **Medallion Architecture**:

```

Raw   →   Silver   →   Gold
CSV       Cleaned     RFM + Clusters

```

- **Raw:** original public dataset (ignored by Git)  
- **Silver:** cleaned and preprocessed parquet files  
- **Gold:** final analytical tables (RFM + cluster labels)

---

## 📁 Repository Structure



```markdown
consumer-segmentation-rfm/
│
├── data/                      # Local only (ignored in Git)
│   ├── raw/
│   ├── silver/
│   └── gold/
│
├── docs/
│   ├── functional_specs.md
│   ├── technical_specs.md
│   ├── data_dictionary.md
│   └── architecture.png
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_preprocessing_pipeline.ipynb
│   └── 03_clustering_results.ipynb
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── clustering.py
│   └── visualization.py
│
├── tests/
│   ├── test_preprocessing.py
│   └── test_rfm.py
│
├── pyproject.toml / requirements.txt
├── .pre-commit-config.yaml
├── Makefile
└── README.md

````

---

## ⚙️ Installation & Setup

### **1. Clone the repository**
```bash
git clone https://github.com/ewertonfl/consumer-segmentation-rfm.git
cd consumer-segmentation-rfm
````

### **2. Setup environment**

Using `Makefile`:

```bash
make setup
```

Or manually:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Running the Pipeline

### **Run full pipeline (load → clean → RFM → clustering):**

```bash
make run
```

### **Run tests**

```bash
make test
```

### **Launch Jupyter notebooks**

```bash
make notebook
```

---

## 📊 Results Included

```
✔️ Clean customer dataset
✔️ RFM table (recency, frequency, monetary)
✔️ Clustering using K-Means / DBSCAN
✔️ Visual insights
✔️ Behavioral profiles for each cluster
✔️ Documentation for business & technical audiences

```
Graphs and insights are located in:

```
notebooks/03_clustering_results.ipynb
```

---

## 🧪 Tests Included

* Data quality checks (Silver layer)
* RFM computation validation
* Output schema verification

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🤝 Contact

If you want to connect, collaborate, discuss Data Engineering, or Data Science:

**🔗 LinkedIn:** [https://www.linkedin.com/in/ewertonfl/](https://www.linkedin.com/in/ewertonfl/)
