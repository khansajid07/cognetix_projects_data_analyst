# 📊 Sales Data Analysis

## 📌 Project Overview

This project analyzes sales data using Python to identify sales trends, top-performing product lines, geographical performance, and other useful business insights.

The project was completed as part of a data analysis internship/task and demonstrates the practical use of Python for data cleaning, exploratory data analysis (EDA), statistical analysis, and data visualization.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand and explore the sales dataset
* Clean and prepare the data for analysis
* Calculate important sales metrics
* Analyze sales by product line
* Analyze sales by country
* Identify top-performing products
* Analyze monthly sales trends
* Create meaningful visualizations
* Extract useful business insights from the data

---

## 🛠️ Technologies & Libraries Used

* **Python 3.10**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical computations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical data visualization
* **Jupyter Notebook** – Interactive analysis environment

---

## 📂 Project Structure

```text
sales-data-analysis/
│
├── analysis.ipynb
├── sales_data_sample.scv
└── README.md

```

> The original dataset can be downloaded from the Kaggle source mentioned below.

---

## 📊 Dataset

The dataset used in this project is the **Sample Sales Data** dataset available on Kaggle.

**Source:** Kaggle – Sample Sales Data

The dataset contains sales-related information such as:

* Order number
* Order date
* Quantity ordered
* Price
* Sales
* Product line
* Product code
* Customer information
* Country
* Deal size

Dataset source:

https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

---

## 🔍 Data Analysis Process

### 1. Data Loading

The dataset was loaded using Pandas:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
```

### 2. Data Understanding

The following operations were performed to understand the dataset:

```python
df.head()
df.info()
df.describe()
df.shape
df.columns
```

These operations helped identify the structure, data types, number of records, and statistical characteristics of the dataset.

---

### 3. Data Cleaning

The dataset was checked for:

* Missing values
* Duplicate records
* Incorrect data types
* Date formatting
* Inconsistent or invalid values

Date columns were converted into appropriate datetime formats where required.

---

### 4. Sales Metrics

Important sales metrics were calculated, including:

* Total Sales
* Average Sales
* Maximum Sale
* Minimum Sale
* Product-line sales
* Country-wise sales

Example:

```python
total_sales = df["SALES"].sum()
average_sales = df["SALES"].mean()
maximum_sale = df["SALES"].max()
minimum_sale = df["SALES"].min()
```

---

## 📈 Visualizations

Several charts were created to understand sales performance visually.

### Product Line Sales

A bar chart was used to compare sales across different product lines.

### Country-wise Sales

Sales performance was analyzed across different countries.

### Monthly Sales Trend

Monthly sales were analyzed to identify trends and changes over time.

### Top Products

The highest-performing products were identified based on total sales.

### Additional Visualizations

Other charts were created using Matplotlib and Seaborn to explore relationships and patterns within the dataset.

---

## 💡 Key Insights

The analysis helps identify:

* Which product lines generate the highest revenue
* Which countries contribute the most to sales
* Which products perform best
* How sales change over time
* Differences in sales performance across categories/product lines
* Overall sales distribution and trends

> Specific numerical findings and charts are available in `analysis.ipynb`.

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Navigate to the Project

```bash
cd sales-data-analysis
```

### 3. Create the Conda Environment

```bash
conda create -n sales-analysis python=3.10
```

### 4. Activate the Environment

```bash
conda activate sales-analysis
```

### 5. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 6. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
analysis.ipynb
```

and run the cells sequentially.

---

## 📌 Important Note About the Dataset

The dataset does not contain a column specifically named `CATEGORY`.

Instead, the `PRODUCTLINE` column was used for product-line/category-level sales analysis.

This project therefore uses the actual structure and column names provided by the Kaggle dataset rather than assuming a predefined schema.

---

## 🚀 Future Improvements

Possible improvements to this project include:

* Creating an interactive dashboard using Power BI or Tableau
* Performing more advanced statistical analysis
* Building sales forecasting models
* Adding customer segmentation
* Performing monthly and yearly growth analysis
* Creating automated reports
* Developing a machine learning model for sales prediction

---

## 👨‍💻 Author

**sajid abdullah**

Data Analysis Intern / Aspiring Data Analyst

### Skills Demonstrated

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Business Analysis

---

## ⭐ Acknowledgements

* Dataset: Kaggle Sample Sales Data
* Tools: Python, Pandas, NumPy, Matplotlib, Seaborn, and Jupyter Notebook
