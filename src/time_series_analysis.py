import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

def run_analysis(merged_data):
    st.title("시계열 분석")
    perform_time_series_analysis(merged_data)

def perform_time_series_analysis(merged_data):
    st.subheader("미곡 생산량 시계열 분석")
    
    # SARIMA 모델
    model = SARIMAX(merged_data['RiceProduction'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit()

    # 예측
    forecast = results.forecast(steps=36)  # 3년 예측
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['RiceProduction'], label='Observed')
    ax.plot(forecast.index, forecast, label='Forecast')
    ax.set_title('Rice Production Forecast')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (ton)')
    ax.legend()
    st.pyplot(fig)

    st.write("모델 요약:")
    st.write(results.summary())

    st.success("Time series analysis completed.")
