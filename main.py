import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.data_loader import load_and_preprocess_data
from src.machine_learning_models import run_analysis as run_ml_models_analysis
from src.correlation_regression_analysis import run_analysis as run_corr_regression_analysis
from src.basic_analysis_2 import display_basic_analysis_2
from src.exploratory_data_analysis import run_exploratory_data_analysis

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
    ("기본 분석", "기본분석2", "탐색적 데이터 분석", "머신러닝 모델", "상관 및 회귀 분석")
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
    st.write(data.set_index('Year_Display'))
    # 농업 구조 변화 그래프
    st.subheader("농업 구조 변화")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['Farmhouseholds'], name="농가 수"), secondary_y=False)
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['PaddyField+Upland'], name="총 경지면적"), secondary_y=True)
    fig.update_layout(title_text="농가 수 및 총 경지면적 변화")
    fig.update_xaxes(title_text="연도")
    fig.update_yaxes(title_text="농가 수", secondary_y=False)
    fig.update_yaxes(title_text="총 경지면적 (ha)", secondary_y=True)
    st.plotly_chart(fig)
    # 작물 생산량 변화 그래프
    st.subheader("작물 생산량 변화")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['RiceProduction'], name="쌀 생산량"))
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['PotatoesProduction'], name="감자 생산량"))
    fig.update_layout(title_text="작물 생산량 변화", xaxis_title="연도", yaxis_title="생산량 (ton)")
    st.plotly_chart(fig)
    # 온도와 강수량 그래프
    st.subheader("기후 변화")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=data['Year_Display'], y=data['precipitation'], name="강수량", opacity=0.5), secondary_y=True)
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['temperature'], name="평균 기온", line=dict(color='red')), secondary_y=False)
    fig.update_layout(title_text="온도 및 강수량 변화")
    fig.update_xaxes(title_text="연도")
    fig.update_yaxes(title_text="평균 기온 (°C)", secondary_y=False)
    fig.update_yaxes(title_text="강수량 (mm)", secondary_y=True)
    fig.update_layout(legend=dict(traceorder="reversed"))
    st.plotly_chart(fig)
    # 대기질 데이터 그래프
    st.subheader("대기질 변화")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['PM10'], name="PM10"))
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['PM2.5'], name="PM2.5"))
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['O3'], name="O3"))
    fig.update_layout(title_text="대기질 변화", xaxis_title="연도", yaxis_title="농도")
    st.plotly_chart(fig)

elif analysis_option == "기본 분석2":
    display_basic_analysis_2(data)

elif analysis_option == "탐색적 데이터 분석":
    run_exploratory_data_analysis(data)

elif analysis_option == "상관 및 회귀 분석":
    run_corr_regression_analysis(data)
    
elif analysis_option == "머신러닝 모델":
    run_ml_models_analysis(data)

        

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 강릉시 데이터 분석 공모전")
