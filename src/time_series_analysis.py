import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

def run_analysis(data):
    st.title("시계열 분석")
    perform_time_series_analysis(data)

def perform_time_series_analysis(data):
    st.subheader("미곡 생산량 시계열 분석")
    
    # 인덱스를 datetime으로 변환
    data_ts = data.copy()
    data_ts.index = pd.to_datetime(data_ts.index + '-01-01')
    
    # SARIMA 모델
    model = SARIMAX(data_ts['RiceProduction'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
    results = model.fit()

    # 예측
    forecast = results.forecast(steps=3)  # 3년 예측
    
    # 그래프 생성
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data_ts.index, data_ts['RiceProduction'], label='Observed')
    ax.plot(forecast.index, forecast, label='Forecast')
    ax.set_title('Rice Production Forecast')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (ton)')
    ax.legend()
    
    # x축 레이블 수정
    ax.set_xticklabels([d.strftime('%Y') for d in ax.get_xticks()])
    
    st.pyplot(fig)

    st.write("모델 요약:")
    st.write(results.summary())

    st.success("Time series analysis completed.")
