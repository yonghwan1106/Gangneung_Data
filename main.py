import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_processing import load_data, preprocess_data

st.title('강릉시 기후변화와 농업 구조 변화 분석')

@st.cache_data
def get_processed_data():
    crop_data, agri_data, air_data, climate_data = load_data()
    return preprocess_data(crop_data, agri_data, air_data, climate_data)

merged_data = get_processed_data()

st.subheader('처리된 데이터')
st.dataframe(merged_data)

st.subheader('연도별 미곡 생산량과 강수량의 관계')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(merged_data.index, merged_data['Rice_Production'], label='Rice Production')
ax.plot(merged_data.index, merged_data['Precipitation'], label='Precipitation')
ax.set_title('Rice Production and Precipitation in Gangneung')
ax.set_xlabel('Year')
ax.set_ylabel('Amount')
ax.legend()
st.pyplot(fig)

st.subheader('농가 수와 경지면적의 변화')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(merged_data.index, merged_data['Total_x'], label='Total Farm Area')
ax.plot(merged_data.index, merged_data['Total_y'], label='Farm Households')
ax.set_title('Changes in Farm Area and Farm Households in Gangneung')
ax.set_xlabel('Year')
ax.set_ylabel('Amount')
ax.legend()
st.pyplot(fig)

st.subheader('주요 변수 간 상관관계')
correlation = merged_data[['Rice_Production', 'Precipitation', 'Total_x', 'Total_y', '(PM10)', '(PM2.5)']].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)

st.subheader('결론 및 시사점')
st.write("""
- 미곡 생산량과 강수량 사이에 양의 상관관계가 있음을 확인할 수 있습니다.
- 농가 수와 경지면적이 감소하는 추세를 보이고 있어, 농업 구조의 변화가 진행 중임을 알 수 있습니다.
- 대기질(PM10, PM2.5)과 농업 생산 사이의 관계도 고려해볼 필요가 있습니다.
- 이러한 분석 결과를 바탕으로 강릉시의 농업 정책 및 기후변화 대응 전략을 수립할 수 있을 것입니다.
""")
