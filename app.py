import streamlit as st
import pandas as pd

st.set_page_config(page_title="Network Anomaly Detector", layout="wide")

st.title("🚨 Network Traffic Anomaly Detection Dashboard")

# Load anomaly results
try:
    df = pd.read_csv("anomaly_results.csv")
except:
    st.error("Run train_model.py first to generate anomaly_results.csv")
    st.stop()

st.subheader("📊 Captured Network Traffic Data")
st.dataframe(df)

# Count anomalies
anomaly_count = (df["anomaly"] == -1).sum()
normal_count = (df["anomaly"] == 1).sum()

col1, col2 = st.columns(2)
col1.metric("🚨 Anomalous Packets", anomaly_count)
col2.metric("✅ Normal Packets", normal_count)

st.subheader("📈 Packet Size Visualization")
st.line_chart(df["packet_size"])

st.subheader("🔎 Anomaly Distribution")
st.bar_chart(df["anomaly"].value_counts())