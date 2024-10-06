import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.data_loader import load_and_preprocess_data
from src.time_series_analysis import run_analysis as run_time_series_analysis
from src.machine_learning_models import run_analysis as run_ml_models_analysis
from src.correlation_regression_analysis import run_analysis as run_corr_regression_analysis
from src.agriculture_structure_analysis import run_analysis as run_agriculture_analysis
from src.basic_analysis_2 import display_basic_analysis_2

# 페이지 설정
st.set_page_config(page_title="강릉시 농업 데이터 분석", layout="wide")

# 데이터 로드
@st.cache_data
def load_data():
    data = load_and_preprocess_data()
    if data is None:
        st.error("데이터 로딩에 실패했습니다. 프로그램을 종료합니다.")
        st.stop()
    
    # 표시용 연도 열 추가
    data['Year_Display'] = data.index.strftime('%Y')
    return data

data = load_data()

# 사이드바 - 상세 분석 메뉴
st.sidebar.title("상세 분석")
analysis_option = st.sidebar.radio(
    "분석 옵션을 선택하세요",
    ("기본 분석", "기본 분석2", "시계열 분석", "머신러닝 모델", "상관 및 회귀 분석", "농업 구조 상세 분석")
)

# 메인 페이지 제목
st.title("강릉시 농업 데이터 분석 (2016-2022)")

if analysis_option == "기본 분석":
    # 기존의 기본 분석 코드...

elif analysis_option == "기본 분석2":
    display_basic_analysis_2(data)

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
