import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_and_preprocess_data
from climate_analysis import analyze_climate
from agriculture_structure_analysis import analyze_agriculture_structure
from correlation_regression_analysis import perform_correlation_regression_analysis
from time_series_analysis import perform_time_series_analysis
from machine_learning_models import apply_machine_learning_models

# 페이지 설정
st.set_page_config(page_title="강릉시 농업 데이터 분석", layout="wide")

# 데이터 로드
@st.cache_data
def load_data():
    return load_and_preprocess_data()

data = load_data()

# 사이드바 - 분석 옵션 선택
analysis_option = st.sidebar.selectbox(
    "분석 옵션을 선택하세요",
    ("데이터 개요", "기후 변화 분석", "농업 구조 변화 분석", "상관관계 및 회귀분석", "시계열 분석", "머신러닝 모델")
)

# 메인 페이지 제목
st.title("강릉시 농업 데이터 분석 (2016-2022)")

if analysis_option == "데이터 개요":
    st.write("## 데이터 개요")
    st.write(data.describe())
    st.write("### 데이터 샘플")
    st.write(data.head())

elif analysis_option == "기후 변화 분석":
    st.write("## 기후 변화 분석")
    fig = analyze_climate(data)
    st.pyplot(fig)

elif analysis_option == "농업 구조 변화 분석":
    st.write("## 농업 구조 변화 분석")
    fig = analyze_agriculture_structure(data)
    st.pyplot(fig)

elif analysis_option == "상관관계 및 회귀분석":
    st.write("## 상관관계 및 회귀분석")
    results = perform_correlation_regression_analysis(data)
    st.write(results)

elif analysis_option == "시계열 분석":
    st.write("## 시계열 분석")
    fig = perform_time_series_analysis(data)
    st.pyplot(fig)

elif analysis_option == "머신러닝 모델":
    st.write("## 머신러닝 모델")
    results = apply_machine_learning_models(data)
    st.write(results)

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 강릉시 데이터 분석 공모전")
