import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import load_and_preprocess_data
from src.time_series_analysis import run_analysis as run_time_series_analysis
from src.machine_learning_models import run_analysis as run_ml_models_analysis
from src.correlation_regression_analysis import run_analysis as run_corr_regression_analysis
from src.agriculture_structure_analysis import run_analysis as run_agriculture_analysis

# 페이지 설정
st.set_page_config(page_title="강릉시 농업 데이터 분석", layout="wide")

# 데이터 로드
@st.cache_data
def load_data():
    data = load_and_preprocess_data()
    if data is None:
        st.error("데이터 로딩에 실패했습니다. 프로그램을 종료합니다.")
        st.stop()
    return data

data = load_data()

# 사이드바 - 상세 분석 메뉴
st.sidebar.title("상세 분석")
analysis_option = st.sidebar.radio(
    "분석 옵션을 선택하세요",
    ("기본 분석", "시계열 분석", "머신러닝 모델", "상관 및 회귀 분석", "농업 구조 상세 분석")
)

# 메인 페이지 제목
st.title("강릉시 농업 데이터 분석 (2016-2022)")

if analysis_option == "기본 분석":
    # 기본 분석 섹션
    st.header("기본 데이터 분석")

    # 데이터 개요
    st.subheader("데이터 개요")
    st.write(data.describe())
    
    # 원본 데이터 표시
    st.subheader("원본 데이터")
    st.write(data)

    # 농업 구조 변화 그래프
    st.subheader("농업 구조 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Farmhouseholds '], label='Number of Farm Households')
    ax.plot(data.index, data['PaddyField+Uplandl'], label='Total Cultivated Area')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

    # 작물 생산량 변화 그래프
    st.subheader("작물 생산량 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['RiceProduction'], label='Rice Production')
    ax.plot(data.index, data['PotatoesProduction'], label='Potato Production')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (ton)')
    ax.legend()
    st.pyplot(fig)

    # 온도와 강수량 그래프
    st.subheader("기후 변화")
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    ax1.plot(data.index, data['temperature'], color='red', label='Temperature')
    ax2.bar(data.index, data['precipitation'], alpha=0.3, color='blue', label='Precipitation')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Temperature (°C)', color='red')
    ax2.set_ylabel('Precipitation (mm)', color='blue')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    st.pyplot(fig)

    # 대기질 데이터 그래프
    st.subheader("대기질 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['PM10'], label='PM10')
    ax.plot(data.index, data['PM2.5'], label='PM2.5')
    ax.plot(data.index, data['O3'], label='O3')
    ax.set_xlabel('Year')
    ax.set_ylabel('Concentration')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "시계열 분석":
    run_time_series_analysis(data)
elif analysis_option == "머신러닝 모델":
    run_ml_models_analysis(data)
elif analysis_option == "상관 및 회귀 분석":
    run_corr_regression_analysis(data)
elif analysis_option == "농업 구조 상세 분석":
    run_agriculture_analysis(data)

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 강릉시 데이터 분석 공모전")
