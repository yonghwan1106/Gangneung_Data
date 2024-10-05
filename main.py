import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import load_and_preprocess_data

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

# 사이드바 - 분석 옵션 선택
analysis_option = st.sidebar.selectbox(
    "분석 옵션을 선택하세요",
    ("데이터 개요", "농업 구조 변화", "작물 생산량 변화", "기후 변화", "대기질 변화")
)

# 메인 페이지 제목
st.title("강릉시 농업 데이터 분석 (2016-2022)")

if analysis_option == "데이터 개요":
    st.write("## 데이터 개요")
    st.write(data.describe())
    st.write("### 데이터 샘플")
    st.write(data)

elif analysis_option == "농업 구조 변화":
    st.write("## 농업 구조 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Farm households '], label='농가 수')
    ax.plot(data.index, data['Total'], label='총 경지면적')
    ax.set_xlabel('연도')
    ax.set_ylabel('값')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "작물 생산량 변화":
    st.write("## 작물 생산량 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Rice Production'], label='쌀 생산량')
    ax.plot(data.index, data['Potatoes Production'], label='감자 생산량')
    ax.set_xlabel('연도')
    ax.set_ylabel('생산량 (톤)')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "기후 변화":
    st.write("## 기후 변화")
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    ax1.plot(data.index, data['temperature'], color='red', label='평균 기온')
    ax2.bar(data.index, data['precipitation'], alpha=0.3, color='blue', label='강수량')
    ax1.set_xlabel('연도')
    ax1.set_ylabel('평균 기온 (°C)', color='red')
    ax2.set_ylabel('강수량 (mm)', color='blue')
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    st.pyplot(fig)

elif analysis_option == "대기질 변화":
    st.write("## 대기질 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['PM10'], label='PM10')
    ax.plot(data.index, data['PM2.5'], label='PM2.5')
    ax.set_xlabel('연도')
    ax.set_ylabel('농도 (μg/m³)')
    ax.legend()
    st.pyplot(fig)

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 강릉시 데이터 분석 공모전")
