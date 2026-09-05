# 🛍️ Retail Analytics & AI-Powered Sales Forecasting System

An end-to-end Retail Analytics and Machine Learning solution developed as a major project for the **Unlox Academy Workshop**. This system includes automated data cleaning, Exploratory Data Analysis (EDA), RFM customer segmentation, Random Forest time-series sales forecasting, dynamic Power BI integration, and a multi-page interactive Streamlit dashboard.

---

## 📌 Project Overview & Key Features

* **Data Engineering & Cleaning:** Automated scripts to handle missing values, correct data types, standardise dates, and engineer new metrics (e.g., total sales, revenue after discounts).
* **Exploratory Data Analysis (EDA):** Deep analytical insights into revenue trends, regional performance, top product categories, and rating distributions.
* **RFM Customer Segmentation:** K-Means Clustering model applied on Recency, Frequency, and Monetary (RFM) values to identify key customer and store profiles.
* **AI Sales Forecasting:** Time-series prediction model built with `RandomForestRegressor` to forecast future store revenue.
* **Interactive Multi-Page Streamlit App:** Clean UI with custom CSS styling and modular pages (`Sales Analysis`, `Store Analysis`, `Product Analysis`, `Forecasting`, `Segmentation`).
* **Power BI Integration:** Dedicated `.pbix` reporting dashboard for business users.

---

## 📊 Dashboard Preview

### 🏠 Main Dashboard

<img width="925" height="346" alt="Screenshot 2026-09-03 090643" src="https://github.com/user-attachments/assets/ddbe80fe-cae9-4f7c-8572-6f45da51b7a3" />


### 📈 Sales & Regional Analytics

The Sales & Regional Analytics section provides category-wise sales and regional revenue visualisations.

<img width="949" height="541" alt="Screenshot 2026-09-03 090654" src="https://github.com/user-attachments/assets/75793b66-be13-42a1-a142-52422b089fea" />


### 🎯 Customer / Store Segmentation

The segmentation section presents RFM values, K-Means clusters, and segment names such as **Top Performers**, **Moderate Performers**, and **Low Activity**.

<img width="1004" height="495" alt="Screenshot 2026-09-03 090703" src="https://github.com/user-attachments/assets/39ff2cd8-b9b1-43c6-b130-c61bb033a4f7" />


### 🔮 AI Daily Sales Forecasting

The forecasting section compares **actual sales** with **predicted sales** over time.

<img width="1036" height="534" alt="Screenshot 2026-09-03 091007" src="https://github.com/user-attachments/assets/978d4364-a0a3-421c-a849-2d60111e41f4" />


---

## 📂 Project Structure

```text
Retail Analytics System/
│
├── assets/                  # Custom CSS styling & media assets
│   ├── style.css
│   └── logo.png
│
├── dashboard/               # Multi-page Streamlit Application
│   ├── app.py               # Main entry script (Home Page)
│   └── pages/               # Sub-pages for interactive navigation
│       ├── 1_Sales_Analysis.py
│       ├── 2_Store_Analysis.py
│       ├── 3_Product_Analysis.py
│       ├── 4_Forecasting.py
│       └── 5_Segmentation.py
│
├── data/                    # Datasets folder
│   ├── raw/                 # Unprocessed raw sales data
│   └── processed/           # Cleaned and processed CSV datasets
│
├── database/                # SQL Database scripts
│   └── retail_analytics.sql # Schema & table creation scripts
│
├── models/                  # Saved Machine Learning models
│   └── sales_forecast.pkl
│
├── powerbi/                 # Power BI Dashboard file & documentation
│   └── Retail_Analytics.pbix
│
├── python/                  # Core Python modules
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── segmentation.py
│   └── forecasting.py
│
├── visualizations/          # Dashboard screenshots & visual outputs
│   ├── dashboard_preview.png
│   ├── sales_regional_analytics.png
│   ├── customer_segmentation.png
│   └── sales_forecasting.png
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Scikit-learn
* Random Forest
* K-Means Clustering
* RFM Analysis
* SQL / MySQL
* Power BI
* Matplotlib
* Seaborn

---

## ▶️ Run the Project Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application

From the project root folder:

```bash
python -m streamlit run dashboard/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📈 Analytics Covered

### Sales Analytics

* Total Revenue
* Total Units Sold
* Total Transactions
* Average Store Rating
* Category Sales Breakdown
* Regional Revenue Share

### Customer / Store Segmentation

* Recency
* Frequency
* Monetary Value
* K-Means Cluster
* Segment Name

### Sales Forecasting

* Daily sales analysis
* Actual vs Predicted Sales
* Time-series forecasting results

---

## 🎓 Project Information

**Project:** Retail Analytics & AI-Powered Sales Forecasting System
**Workshop:** Unlox Academy Workshop
**Domain:** Data Analytics, Machine Learning & Business Intelligence

---

## 👨‍💻 Author

**Vivek Jadhav**


---


