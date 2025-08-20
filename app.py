import streamlit as st
import pandas as pd

st.title("📊 Customer Data Analysis Agent")

st.write("Analyze individual customers or upload a dataset for insights.")

# --- Option 1: Manual Customer Entry ---
st.subheader("Manual Customer Entry")
name = st.text_input("Customer Name")
age = st.number_input("Age", min_value=10, max_value=100, step=1)
income = st.number_input("Monthly Income ($)", min_value=0, step=100)
purchases = st.number_input("Number of Purchases Last 6 Months", min_value=0, step=1)
satisfaction = st.slider("Customer Satisfaction (1=Low, 5=High)", 1, 5, 3)

if st.button("Analyze Customer"):
    st.subheader(f"Analysis for {name if name else 'Customer'}")

    if income > 5000 and purchases > 10:
        st.write("💎 High-Value Customer (Priority retention)")
    elif satisfaction <= 2:
        st.write("⚠️ At-Risk Customer (Low satisfaction)")
    elif purchases < 2:
        st.write("⚠️ Low Engagement (Consider reactivation campaign)")
    else:
        st.write("✅ Regular Customer (Maintain relationship)")

# --- Option 2: Upload CSV ---
st.subheader("Batch Customer Analysis (Upload CSV)")
uploaded_file = st.file_uploader("Upload customer data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("📄 Uploaded Data")
    st.dataframe(df.head())

    def analyze_row(row):
        if row["Income"] > 5000 and row["Purchases"] > 10:
            return "High-Value"
        elif row["Satisfaction"] <= 2:
            return "At-Risk"
        elif row["Purchases"] < 2:
            return "Low Engagement"
        else:
            return "Regular"

    df["Customer_Analysis"] = df.apply(analyze_row, axis=1)

    st.subheader("📊 Analysis Results")
    st.dataframe(df)

    # Download option
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Results", data=csv, file_name="customer_analysis.csv")
