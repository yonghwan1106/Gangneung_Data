import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import load_and_preprocess_data

# 페이지 설정
st.set_page_config(page_title="Gangneung Agricultural Data Analysis", layout="wide")

# 데이터 로드
@st.cache_data
def load_data():
    data = load_and_preprocess_data()
    if data is None:
        st.error("Failed to load data. The program will terminate.")
        st.stop()
    return data

data = load_data()

# 사이드바 - 분석 옵션 선택
analysis_option = st.sidebar.selectbox(
    "Select analysis option",
    ("Data Overview", "Agricultural Structure Change", "Crop Production Change", "Climate Change", "Air Quality Change")
)

# 메인 페이지 제목
st.title("Gangneung Agricultural Data Analysis (2016-2022)")

if analysis_option == "Data Overview":
    st.write("## Data Overview")
    st.write(data.describe())
    st.write("### Data Sample")
    st.write(data)

elif analysis_option == "Agricultural Structure Change":
    st.write("## Agricultural Structure Change")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Farmhouseholds '], label='Number of FarmHouseholds')
    ax.plot(data.index, data['Total'], label='Total Cultivated Area')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "Crop Production Change":
    st.write("## Crop Production Change")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Rice Production'], label='RiceProduction')
    ax.plot(data.index, data['Potatoes Production'], label='PotatoProduction')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (ton)')
    ax.legend()
    st.pyplot(fig)

elif analysis_option == "Climate Change":
    st.write("## Climate Change")
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

elif analysis_option == "Air Quality Change":
    st.write("## Air Quality Change")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['PM10'], label='PM10')
    ax.plot(data.index, data['PM2.5'], label='PM2.5')
    ax.set_xlabel('Year')
    ax.set_ylabel('Concentration (μg/m³)')
    ax.legend()
    st.pyplot(fig)

# 푸터
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Gangneung Data Analysis Competition")
