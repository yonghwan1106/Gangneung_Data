import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_and_preprocess_data
from src.agriculture_structure_analysis import analyze_agriculture_structure

def main():
    st.title("강릉시 농업 구조 및 기후 변화 분석")

    # 데이터 로드
    data = load_and_preprocess_data()

    # 데이터 개요 표시
    st.header("데이터 개요")
    st.write(data.head())
    st.write(f"데이터 기간: {data.index.min().year} - {data.index.max().year}")

    # 농업 구조 분석
    st.header("농업 구조 분석")
    analyze_agriculture_structure(data)

    # 기후 변화 분석
    st.header("기후 변화 분석")
    analyze_climate_change(data)

    # 농업 생산성 분석
    st.header("농업 생산성 분석")
    analyze_agricultural_productivity(data)

    # 상관관계 분석
    st.header("변수 간 상관관계 분석")
    correlation_analysis(data)

def analyze_climate_change(data):
    st.subheader("연간 평균 기온 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['mean'], marker='o')
    ax.set_xlabel('연도')
    ax.set_ylabel('평균 기온 (°C)')
    ax.set_title('연간 평균 기온 변화')
    st.pyplot(fig)

    st.subheader("연간 강수량 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data.index, data['precipitation'])
    ax.set_xlabel('연도')
    ax.set_ylabel('강수량 (mm)')
    ax.set_title('연간 강수량 변화')
    st.pyplot(fig)

def analyze_agricultural_productivity(data):
    st.subheader("농업 생산성 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['productivity'], marker='o')
    ax.set_xlabel('연도')
    ax.set_ylabel('생산성 (톤/헥타르)')
    ax.set_title('농업 생산성 변화')
    st.pyplot(fig)

def correlation_analysis(data):
    corr_vars = ['farm_households', 'total_cultivated_area', 'total_production', 
                 'mean', 'precipitation', 'productivity']
    corr_matrix = data[corr_vars].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('변수 간 상관관계')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
