# 2_2_exploratory_data_analysis.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.statespace.sarimax import SARIMAX
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# 데이터 로드 및 전처리
@st.cache_data
def load_and_process_data():
    data = pd.read_csv('total_data.csv')
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')
    data.set_index('Year', inplace=True)
    return data

data = load_and_process_data()

def exploratory_data_analysis():
    st.title("2.2 Exploratory Data Analysis (EDA)")

    st.header("Data Overview")
    st.write(data.describe())

    st.header("Data Visualization")
    
    # 시계열 데이터 시각화
    st.subheader("Time Series of Key Variables")
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(x=data.index, y=data['RiceProduction'], name='Rice Production'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['temperature'], name='Temperature'), row=2, col=1)
    fig.add_trace(go.Bar(x=data.index, y=data['precipitation'], name='Precipitation'), row=3, col=1)
    fig.update_layout(height=600, title_text="Key Variables Over Time")
    st.plotly_chart(fig)

def time_series_decomposition():
    st.header("1. 미곡생산량 시계열분석")
    rice_production = data['RiceProduction']
    result = seasonal_decompose(rice_production, model='additive', period=1)
    
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(x=data.index, y=result.observed, mode='lines', name='관측값'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=result.trend, mode='lines', name='추세'), row=2, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=result.seasonal, mode='lines', name='계절성'), row=3, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=result.resid, mode='lines', name='잔차'), row=4, col=1)
    
    fig.update_layout(height=800, title_text='미곡생산량 시계열 분해')
    st.plotly_chart(fig)

def correlation_matrix():
    st.header("2. 주요 변수간 상관관계 행렬")
    corr_vars = ['temperature', 'precipitation', 'Farmhouseholds', 'PaddyField+Upland', 'RiceProduction', 'PotatoesProduction']
    corr_matrix = data[corr_vars].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Viridis'))
    
    fig.update_layout(title='주요 변수간 상관관계 행렬')
    st.plotly_chart(fig)

def random_forest_importance():
    st.header("3. RandomForest 특성 중요도")
    X = data[['precipitation', 'Farmhouseholds', 'temperature', 'PaddyField+Upland']]
    y = data['RiceProduction']
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X, y)
    
    importance = rf.feature_importances_
    features = X.columns
    
    fig = go.Figure(data=[go.Bar(x=features, y=importance)])
    fig.update_layout(title='RandomForest 특성 중요도', xaxis_title='특성', yaxis_title='중요도')
    st.plotly_chart(fig)

def sarima_forecast():
    st.header("4. SARIMA 모델을 이용한 미곡 생산량 예측")
    y = data['RiceProduction']
    
    model = SARIMAX(y, order=(1,1,1), seasonal_order=(1,1,1,1))
    results = model.fit()
    
    forecast = results.forecast(steps=3)
    forecast_index = pd.date_range(start=y.index[-1] + pd.DateOffset(years=1), periods=3, freq='Y')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y.index, y=y, mode='lines', name='실제 생산량'))
    fig.add_trace(go.Scatter(x=forecast_index, y=forecast, mode='lines', name='예측 생산량', line=dict(dash='dash')))
    
    fig.update_layout(title='SARIMA 모델을 이용한 미곡 생산량 예측', xaxis_title='연도', yaxis_title='생산량')
    st.plotly_chart(fig)

def xgboost_predictions():
    st.header("5. XGBoost 모델의 미곡 생산량 예측")
    X = data[['precipitation', 'Farmhouseholds', 'temperature', 'PaddyField+Upland']]
    y = data['RiceProduction']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    fig = go.Figure(data=go.Scatter(x=y_test, y=y_pred, mode='markers'))
    fig.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()], mode='lines', name='완벽한 예측'))
    
    fig.update_layout(title='XGBoost 모델의 미곡 생산량 예측', xaxis_title='실제 생산량', yaxis_title='예측 생산량')
    st.plotly_chart(fig)

def main():
    exploratory_data_analysis()
    time_series_decomposition()
    correlation_matrix()
    random_forest_importance()
    sarima_forecast()
    xgboost_predictions()

if __name__ == "__main__":
    main()
