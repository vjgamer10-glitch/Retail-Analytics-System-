import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Page Config
st.set_page_config(
    page_title="Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "Retail_Sales_Data_Cleaned.csv"
SEGMENT_PATH = BASE_DIR / "data" / "processed" / "Customer_Segments.csv"
FORECAST_PATH = BASE_DIR / "data" / "processed" / "Sales_Forecast_Results.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

st.title("📊 Retail Analytics & AI-Powered Sales Forecasting")

# Sidebar Filters
st.sidebar.header("Filter Data")
region = st.sidebar.multiselect(
    "Select Region:",
    options=df["region"].unique(),
    default=df["region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category:",
    options=df["product_category"].unique(),
    default=df["product_category"].unique()
)

filtered_df = df[(df["region"].isin(region)) & (df["product_category"].isin(category))]

# Top KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{filtered_df['revenue'].sum():,.2f}")
col2.metric("Total Units Sold", f"{filtered_df['units_sold'].sum():,}")
col3.metric("Total Transactions", f"{len(filtered_df):,}")
col4.metric("Avg Store Rating", f"{filtered_df['store_rating'].mean():.2f} ⭐")

st.markdown("---")

# Visualizations Tab
tab1, tab2, tab3 = st.tabs(["📈 Sales & Regional Analytics", "🎯 Customer Segmentation", "🔮 Sales Forecasting"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Category Sales Breakdown")
        cat_sales = filtered_df.groupby("product_category")["total_sales"].sum()
        st.bar_chart(cat_sales)
    with col2:
        st.subheader("Regional Revenue Share")
        reg_sales = filtered_df.groupby("region")["revenue"].sum()
        st.line_chart(reg_sales)

with tab2:
    st.subheader("Store / Customer Segmentation (RFM + K-Means)")
    if SEGMENT_PATH.exists():
        seg_df = pd.read_csv(SEGMENT_PATH)
        st.dataframe(seg_df.head(10), use_container_width=True)
    else:
        st.warning("Customer Segments file not found. Run segmentation.py first!")

with tab3:
    st.subheader("AI Daily Sales Forecasting Results")
    if FORECAST_PATH.exists():
        forecast_df = pd.read_csv(FORECAST_PATH)
        forecast_df['date'] = pd.to_datetime(forecast_df['date'])
        st.line_chart(forecast_df.set_index('date')[['actual_sales', 'predicted_sales']])
    else:
        st.warning("Forecast data not found. Run forecasting.py first!")