import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import load_and_preprocess_data
from src.time_series_analysis import run_analysis as run_time_series_analysis
from src.machine_learning_models import run_analysis as run_ml_models_analysis
from src.correlation_regression_analysis import run_analysis as run_corr_regression_analysis
from src.climate_analysis import run_analysis as run_climate_analysis
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

# 메인 페이지 제목
st.title("강릉시 농업 데이터 분석 (2016-2022)")

# 기본 분석 섹션
st.header("기본 데이터 분석")

# 데이터 개요
st.subheader("데이터 개요")
st.write(data.describe())

# 농업 구조 변화 그래프
st.subheader("농업 구조 변화")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data.index, data['Farmhouseholds '], label='Number of Farm Households')
ax.plot(data.index, data['Total'], label='Total Cultivated Area')
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

# 기후 변화 그래프
st.subheader("기후 변화")
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()
ax1.plot(data.index, data['temperature'], color='red', label='Average Temperature')
ax2.bar(data.index, data['precipitation'], alpha=0.3, color='blue', label='Precipitation')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Temperature (°C)', color='red')
ax2.set_ylabel('Precipitation (mm)', color='blue')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
st.pyplot(fig)

# 상세 분석 섹션
st.header("상세 분석")
analysis_option = st.selectbox(
    "분석 옵션을 선택하세요",
    ("선택하세요", "시계열 분석", "머신러닝 모델", "상관 및 회귀 분석", "기후 상세 분석", "농업 구조 상세 분석")
)

if analysis_option == "시계열 분석":
    run_time_series_analysis(data)
elif analysis_option == "머신러닝 모델":
    run_ml_models_analysis(data)
elif analysis_option == "상관 및 회귀 분석":
    run_corr_regression_analysis(data)
elif analysis_option == "기후 상세 분석":
    run_climate_analysis(data)
elif analysis_option == "농업 구조 상세 분석":
    run_agriculture_analysis(data)

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 강릉시 데이터 분석 공모전")
