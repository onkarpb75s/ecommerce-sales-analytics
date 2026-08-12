import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "data" / "orders.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

st.set_page_config(page_title="E-Commerce Analytics Dashboard", layout="wide")
st.title("E-Commerce Sales & Customer Analytics")
st.caption("Portfolio project: Python • SQL • Pandas • Plotly • Streamlit")

with st.sidebar:
    st.header("Filters")
    categories = st.multiselect(
        "Category", sorted(df["category"].unique()), default=sorted(df["category"].unique())
    )
    channels = st.multiselect(
        "Channel", sorted(df["channel"].unique()), default=sorted(df["channel"].unique())
    )
    regions = st.multiselect(
        "Region", sorted(df["region"].unique()), default=sorted(df["region"].unique())
    )

filtered = df[
    df["category"].isin(categories)
    & df["channel"].isin(channels)
    & df["region"].isin(regions)
]

revenue = filtered["revenue"].sum()
profit = filtered["profit"].sum()
orders = filtered["order_id"].nunique()
aov = revenue / orders if orders else 0
margin = profit / revenue if revenue else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue", f"${revenue:,.0f}")
c2.metric("Profit", f"${profit:,.0f}")
c3.metric("Orders", f"{orders:,}")
c4.metric("Profit Margin", f"{margin:.1%}")

monthly = filtered.groupby("month", as_index=False).agg(revenue=("revenue","sum"), profit=("profit","sum"))
fig1 = px.line(monthly, x="month", y="revenue", markers=True, title="Monthly Revenue")
st.plotly_chart(fig1, use_container_width=True)

left, right = st.columns(2)

cat = filtered.groupby("category", as_index=False).agg(revenue=("revenue","sum")).sort_values("revenue", ascending=False)
fig2 = px.bar(cat, x="category", y="revenue", title="Revenue by Category")
left.plotly_chart(fig2, use_container_width=True)

reg = filtered.groupby("region", as_index=False).agg(profit=("profit","sum")).sort_values("profit", ascending=False)
fig3 = px.bar(reg, x="region", y="profit", title="Profit by Region")
right.plotly_chart(fig3, use_container_width=True)

st.subheader("Top Products")
top_products = (
    filtered.groupby(["product_name","category"], as_index=False)
    .agg(revenue=("revenue","sum"), profit=("profit","sum"))
    .sort_values("revenue", ascending=False)
    .head(10)
)
st.dataframe(top_products, use_container_width=True, hide_index=True)
