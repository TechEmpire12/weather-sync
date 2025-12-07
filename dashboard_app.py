import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os

# Constants
CSV_FILE = 'weather_data.csv'

st.set_page_config(
    page_title="Abia State Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Abia State Agricultural Weather Dashboard")
st.markdown("Real-time weather monitoring for agricultural zones in Abia State.")

def load_data():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame()
    try:
        df = pd.read_csv(CSV_FILE)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Auto-refresh logic
if st.button('Refresh Data'):
    st.rerun()

# Load data
df = load_data()

if df.empty:
    st.warning("No data found. Please ensure the data collector script is running.")
else:
    # Get latest data for each zone
    latest_df = df.sort_values('timestamp').groupby('zone').tail(1)
    
    # Key Metrics Display
    st.subheader("Current Conditions")
    cols = st.columns(len(latest_df))
    
    for idx, (_, row) in enumerate(latest_df.iterrows()):
        with cols[idx]:
            st.metric(
                label=f"{row['zone']}",
                value=f"{row['temperature']} °C",
                delta=f"Rain: {row['rain']} mm"
            )

    # Charts
    st.subheader("Weather Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Temperature Trends")
        fig_temp = px.line(df, x='timestamp', y='temperature', color='zone', 
                          title='Temperature over Time', markers=True)
        st.plotly_chart(fig_temp, use_container_width=True)
        
    with col2:
        st.markdown("### Rainfall Trends")
        fig_rain = px.line(df, x='timestamp', y='rain', color='zone', 
                          title='Rainfall over Time', markers=True)
        st.plotly_chart(fig_rain, use_container_width=True)

    # Raw Data
    with st.expander("View Raw Data"):
        st.dataframe(df.sort_values('timestamp', ascending=False))

st.caption("Data updates automatically when the collector script runs. Click 'Refresh Data' to see the latest.")
