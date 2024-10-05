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
    ax.plot(data.index, data['Farmhouseholds '], label='Number of Farm Households')
    ax.plot(data.index, data['Total'], label='Total Cultivated Area')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "작물 생산량 변화":
    st.write("## 작물 생산량 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['RiceProduction'], label='Rice Production')
    ax.plot(data.index, data['PotatoesProduction'], label='Potato Production')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (ton)')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "기후 변화":
    st.write("## 기후 변화")
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

elif analysis_option == "대기질 변화":
    st.write("## 대기질 변화")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['PM10'], label='PM10')
    ax.plot(data.index, data['PM2.5'], label='PM2.5')
    ax.set_xlabel('Year')
    ax.set_ylabel('Concentration (μg/m³)')
    ax.legend()
    st.pyplot(fig)

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 강릉시 데이터 분석 공모전")
