import streamlit as st
import pandas as pd
import datetime
from utils.pricing_logic import suggest_price # type: ignore

import os
os.makedirs("data", exist_ok=True)


st.set_page_config(page_title="Retailer Dashboard", page_icon="🛍")
st.title("🛍 AI-Powered Retailer Dashboard")

st.markdown("Welcome! This smart dashboard helps you decide the best price for your product using AI magic. 🧠✨")

st.header("📦 Enter Product Details")

product_name = st.text_input("Product Name")
base_price = st.number_input("Base Price (₹)", min_value=0.0)
demand = st.selectbox("Demand Level", ["Low", "Medium", "High"])
season = st.selectbox("Season / Month", ["Winter", "Spring", "Summer", "Autumn"])
rating = st.slider("Customer Rating (0 to 5)", 0.0, 5.0, step=0.1)
competitor_price = st.number_input("Competitor Price (₹)", min_value=0.0)
submit = st.button("💡 Suggest Price")


if submit and product_name:
    suggested_price = suggest_price(base_price, demand, season, rating, competitor_price)
    st.success(f"✅ Suggested Price for *{product_name}*: ₹{suggested_price:.2f}")
    
    
    if demand == "High":
        st.warning("📈 High demand this week! Great time to sell.")
    if rating >= 4.5:
        st.info("🌟 Your product has great ratings! Customers love it.")

    # Summary
    st.subheader("📄 Product Summary")
    st.markdown(f"""
    - *Product:* {product_name}  
    - *Base Price:* ₹{base_price}  
    - *Demand:* {demand}  
    - *Season:* {season}  
    - *Rating:* {rating}  
    - *Competitor Price:* ₹{competitor_price}  
    - *Final AI Price:* ₹{suggested_price:.2f}
    """)

    # Graph (dummy price trend)
    st.subheader("📊 Seasonal Price Trend")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    prices = [base_price * (1 + i * 0.05) for i in range(8)]  
    df = pd.DataFrame({"Month": months, "Estimated Price": prices})
    st.line_chart(df.set_index("Month"))

    # Best month to sell
    best_month = months[-1]
    st.success(f"🗓 Best Month to Sell: *{best_month}*")

    # Save data
    data = {
        "Date": [datetime.date.today()],
        "Product": [product_name],
        "Suggested Price": [suggested_price]
    }
    df_save = pd.DataFrame(data)
    df_save.to_csv("data/history.csv", mode='a', header=False, index=False)
    st.caption("✅ Saved to history.")
else:
    st.info("Please enter your product name to get started.")