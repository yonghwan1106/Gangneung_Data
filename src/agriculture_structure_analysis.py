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
    
    # 'farm_households' 열이 있는지 확인
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

    # 농가인구 변화
    if 'farm_population' in data.columns:
        st.subheader("농가인구 변화")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(data.index, data['farm_population'], label='Farm Population')
        ax.set_title('Changes in Farm Population')
        ax.set_xlabel('Year')
        ax.set_ylabel('Farm Population')
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("농가인구 데이터를 찾을 수 없습니다.")

    # 경지면적 변화
    area_columns = ['total_cultivated_area', 'paddy_field_area', 'upland_area']
    if all(col in data.columns for col in area_columns):
        st.subheader("경지면적 변화")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(data.index, data['total_cultivated_area'], label='Total')
        ax.plot(data.index, data['paddy_field_area'], label='Paddy Field')
        ax.plot(data.index, data['upland_area'], label='Upland')
        ax.set_title('Changes in Cultivated Area')
        ax.set_xlabel('Year')
        ax.set_ylabel('Area (ha)')
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("경지면적 데이터를 찾을 수 없습니다.")

    # 농가 유형 변화 (전업농 vs 겸업농)
    if 'full_time_ratio' in data.columns and 'part_time_ratio' in data.columns:
        st.subheader("농가 유형 변화 (전업농 vs 겸업농)")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.stackplot(data.index, data['full_time_ratio'], data['part_time_ratio'], 
                     labels=['Full-time', 'Part-time'])
        ax.set_title('Changes in Farm Type Ratio')
        ax.set_xlabel('Year')
        ax.set_ylabel('Ratio')
        ax.legend(loc='upper left')
        st.pyplot(fig)
    else:
        st.warning("농가 유형 비율 데이터를 찾을 수 없습니다.")

    # 농업 생산성 변화
    if 'productivity' in data.columns:
        st.subheader("농업 생산성 변화")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(data.index, data['productivity'])
        ax.set_title('Changes in Agricultural Productivity')
        ax.set_xlabel('Year')
        ax.set_ylabel('Production per hectare')
        st.pyplot(fig)
    else:
        st.warning("농업 생산성 데이터를 찾을 수 없습니다.")

    st.success("농업 구조 분석이 완료되었습니다.")
