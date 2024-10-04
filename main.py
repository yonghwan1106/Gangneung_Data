import streamlit as st
from src import data_loader, agriculture_structure_analysis, climate_analysis, \
                correlation_regression_analysis, machine_learning_models, time_series_analysis
import src.data_loader as data_loader

st.title('강릉시 기후변화와 농업 구조 변화 분석')

# 데이터 로드
data = data_loader.load_and_preprocess_data()


# 사이드바 메뉴
analysis_option = st.sidebar.selectbox(
    '분석 옵션 선택',
    ['농업 구조 분석', '기후 분석', '상관 및 회귀 분석', '머신러닝 모델', '시계열 분석']
)

if analysis_option == '농업 구조 분석':
    agriculture_structure_analysis.run_analysis(data)
elif analysis_option == '기후 분석':
    climate_analysis.run_analysis(data)
elif analysis_option == '상관 및 회귀 분석':
    correlation_regression_analysis.run_analysis(data)
elif analysis_option == '머신러닝 모델':
    machine_learning_models.run_analysis(data)
elif analysis_option == '시계열 분석':
    time_series_analysis.run_analysis(data)

# 결론 및 시사점
st.subheader('결론 및 시사점')
st.write("""
    [여기에 분석 결과에 따른 결론 및 시사점을 작성합니다.]
""")
