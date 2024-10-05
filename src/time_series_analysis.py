import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

def run_analysis(data):
    st.title("시계열 분석")
    perform_time_series_analysis(data)

def perform_time_series_analysis(data):
    st.subheader("미곡 생산량 시계열 분석")
    
    # 데이터 준비
    data_ts = data.copy()
    if not isinstance(data_ts.index, pd.DatetimeIndex):
        data_ts.index = pd.to_datetime(data_ts.index)
    
    # SARIMA 모델
    model = SARIMAX(data_ts['RiceProduction'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
    results = model.fit()

    # 예측
    forecast = results.forecast(steps=3)  # 3년 예측
    
    # 그래프 생성
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data_ts.index, data_ts['RiceProduction'], label='Observed')
    ax.plot(pd.date_range(start=data_ts.index[-1], periods=4, freq='Y')[1:], forecast, label='Forecast')
    ax.set_title('Rice Production Forecast')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (ton)')
    ax.legend()
    
    # x축 레이블 수정
    ax.set_xticks(pd.date_range(start=data_ts.index[0], end=forecast.index[-1], freq='Y'))
    ax.set_xticklabels([d.strftime('%Y') for d in ax.get_xticks()])
    
    st.pyplot(fig)

    st.write("모델 요약:")
    st.write(results.summary())

    st.success("Time series analysis completed.")
