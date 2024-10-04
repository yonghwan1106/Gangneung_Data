import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def run_analysis(merged_data):
    st.title("기후 분석")
    analyze_climate(merged_data)

def analyze_climate(merged_data):
    # 연간 평균 기온 추이
    st.subheader("연간 평균 기온 추이")
    fig, ax = plt.subplots(figsize=(12, 6))
    yearly_temp = merged_data.resample('Y')['Temperature'].mean()
    ax.plot(yearly_temp.index.year, yearly_temp.values)
    ax.set_title('Annual Average Temperature Trend')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    st.pyplot(fig)

    # 연간 강수량 변화
    st.subheader("연간 강수량 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    yearly_precip = merged_data.resample('Y')['Precipitation'].sum()
    ax.bar(yearly_precip.index.year, yearly_precip.values)
    ax.set_title('Annual Precipitation')
    ax.set_xlabel('Year')
    ax.set_ylabel('Precipitation (mm)')
    st.pyplot(fig)

    # 계절별 평균 기온 변화
    st.subheader("계절별 평균 기온 변화")
    merged_data['Season'] = pd.to_datetime(merged_data.index).month.map({1:'Winter', 2:'Winter', 3:'Spring', 
                                                                         4:'Spring', 5:'Spring', 6:'Summer',
                                                                         7:'Summer', 8:'Summer', 9:'Fall',
                                                                         10:'Fall', 11:'Fall', 12:'Winter'})
    seasonal_temp = merged_data.groupby(['Season', merged_data.index.year])['Temperature'].mean().unstack()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(seasonal_temp, cmap='YlOrRd', annot=True, ax=ax)
    ax.set_title('Seasonal Average Temperature')
    st.pyplot(fig)

    st.success("Climate analysis completed.")
