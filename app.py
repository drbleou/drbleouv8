import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dr Bleou Hybrid Pro", page_icon="📈", layout="wide")

st.title("📈 Dr Bleou Hybrid Pro — Render Ready")

with st.sidebar:
    st.header("Environment")
    st.write({
        "PYTHON_VERSION": os.environ.get("PYTHON_VERSION"),
        "BITGET_API_KEY": "✅ set" if os.environ.get("BITGET_API_KEY") else "⚠️ missing",
        "TELEGRAM_BOT_TOKEN": "✅ set" if os.environ.get("TELEGRAM_BOT_TOKEN") else "⚠️ missing",
    })

# demo timeseries
x = np.arange(0, 500)
y = np.sin(x/20.0) * 8 + 100 + np.random.randn(len(x)) * 0.5
df = pd.DataFrame({"t": pd.date_range("2024-01-01", periods=len(x), freq="min"), "price": y})

col1, col2 = st.columns((2,1))

with col1:
    st.subheader("Demo Price")
    fig = px.line(df, x="t", y="price", labels={"t":"Time","price":"Price"})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Stats")
    st.metric("Last", f"{df['price'].iloc[-1]:.2f}")
    st.metric("Mean", f"{df['price'].mean():.2f}")
    st.metric("Std", f"{df['price'].std():.2f}")

st.success("Running on Render with Python 3.11 wheels only. No native builds.")
