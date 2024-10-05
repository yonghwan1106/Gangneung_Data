import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def run_analysis(data):
    st.title("농업 구조 분석")
    analyze_agriculture_structure(data)

def analyze_agriculture_structure(data):
    st.write("데이터셋의 열:", data.columns.tolist())
    
    # 농가 수 변화
    st.subheader("농가 수 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['Farmhouseholds'], label='Farm Households')
    ax.set_title('Changes in Farm Households')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Farm Households')
    ax.legend()
    st.pyplot(fig)

    # 경지면적 변화
    st.subheader("경지면적 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['PaddyField+Upland'], label='Total')
    ax.plot(data.index, data['PaddyField'], label='Paddy Field')
    ax.plot(data.index, data['Upland'], label='Upland')
    ax.set_title('Changes in Cultivated Area')
    ax.set_xlabel('Year')
    ax.set_ylabel('Area (ha)')
    ax.legend()
    st.pyplot(fig)

    # 농가 유형 변화 (전업농 vs 겸업농)
    st.subheader("농가 유형 변화 (전업농 vs 겸업농)")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.stackplot(data.index, data['fullTime'], data['partTime'], 
                 labels=['Full-time', 'Part-time'])
    ax.set_title('Changes in Farm Type Ratio')
    ax.set_xlabel('Year')
    ax.set_ylabel('Ratio')
    ax.legend(loc='upper left')
    st.pyplot(fig)

    # 농업 생산성 변화
    st.subheader("농업 생산성 변화")
    data['productivity'] = (data['RiceProduction'] + data['PotatoesProduction']) / data['Total']
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['productivity'])
    ax.set_title('Changes in Agricultural Productivity')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production per hectare')
    st.pyplot(fig)

    st.success("농업 구조 분석이 완료되었습니다.")
