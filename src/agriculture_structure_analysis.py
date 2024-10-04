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
    
    # 'Farm_Households' 열이 있는지 확인
    if 'farm_households' in data.columns:
        column_name = 'farm_households'
    elif 'Farm_Households' in data.columns:
        column_name = 'Farm_Households'
    else:
        st.error("농가 수 데이터를 찾을 수 없습니다.")
        return

    # 농가 수 변화
    st.subheader("농가 수 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data[column_name], label='Farm Households')
    ax.set_title('Changes in Farm Households')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Farm Households')
    ax.legend()
    st.pyplot(fig)

def analyze_agriculture_structure(merged_data):
    # 농가 수 및 농가인구 변화
    st.subheader("농가 수 및 농가인구 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['Farm_Households'], label='Farm Households')
    ax.plot(merged_data.index, merged_data['Farm_Population'], label='Farm Population')
    ax.set_title('Changes in Farm Households and Population')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number')
    ax.legend()
    st.pyplot(fig)

    # 경지면적 변화
    st.subheader("경지면적 변화")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['Total_Cultivated_Area'], label='Total')
    ax.plot(merged_data.index, merged_data['Paddy_Field_Area'], label='Paddy Field')
    ax.plot(merged_data.index, merged_data['Upland_Area'], label='Upland')
    ax.set_title('Changes in Cultivated Area')
    ax.set_xlabel('Year')
    ax.set_ylabel('Area (ha)')
    ax.legend()
    st.pyplot(fig)

    # 농가 유형 변화 (전업농 vs 겸업농)
    st.subheader("농가 유형 변화 (전업농 vs 겸업농)")
    merged_data['Full_time_ratio'] = merged_data['Full_time_farm'] / merged_data['Farm_Households']
    merged_data['Part_time_ratio'] = merged_data['Part_time_farm'] / merged_data['Farm_Households']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.stackplot(merged_data.index, merged_data['Full_time_ratio'], merged_data['Part_time_ratio'], 
                 labels=['Full-time', 'Part-time'])
    ax.set_title('Changes in Farm Type Ratio')
    ax.set_xlabel('Year')
    ax.set_ylabel('Ratio')
    ax.legend(loc='upper left')
    st.pyplot(fig)

    # 농업 생산성 변화
    st.subheader("농업 생산성 변화")
    merged_data['Productivity'] = merged_data['Total_Production'] / merged_data['Total_Cultivated_Area']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['Productivity'])
    ax.set_title('Changes in Agricultural Productivity')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production per hectare')
    st.pyplot(fig)

    st.success("Agriculture structure analysis completed.")
