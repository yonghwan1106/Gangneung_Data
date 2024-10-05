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
    yearly_temp = merged_data['temperature']
    ax.plot(yearly_temp.index, yearly_temp.values)
    ax.set_title('Annual Average Temperature Trend')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')
    st.pyplot(fig)

    # 연간 강수량 변화
    st.subheader("연간 강수량 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    yearly_precip = merged_data['precipitation']
    ax.bar(yearly_precip.index, yearly_precip.values)
    ax.set_title('Annual Precipitation')
    ax.set_xlabel('Year')
    ax.set_ylabel('Precipitation (mm)')
    st.pyplot(fig)

    st.success("Climate analysis completed.")
