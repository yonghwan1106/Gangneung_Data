import streamlit as st
from src import data_loader, agriculture_structure_analysis, climate_analysis, \
                correlation_regression_analysis, machine_learning_models, time_series_analysis

def main():
    st.title('강릉시 기후변화와 농업 구조 변화 분석')

    # 데이터 로드
    data = data_loader.load_and_preprocess_data()
    
    # 데이터 확인
    st.write("데이터셋의 열:", data.columns.tolist())
    st.write("데이터 샘플:", data.head())

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
    1. 기후변화의 영향: 강수량 변동성 증가가 작물 생산량의 불안정성을 초래하고 있습니다.
    2. 농업 구조의 변화: 소규모 농가의 증가와 경지면적의 감소 추세가 관찰됩니다.
    3. 작물별 기후 민감도: 미곡은 강수량 증가에 긍정적, 서류는 부정적 영향을 받는 것으로 나타났습니다.
    4. 농업 생산성: 농가당 경지면적 감소에도 불구하고, 기술 혁신으로 생산성이 유지되고 있습니다.
    5. 환경-농업 상호작용: 대기질 개선이 농업 생산성에 긍정적 영향을 미치는 것으로 추정됩니다.

    이러한 분석 결과를 바탕으로, 강릉시는 기후변화에 대응한 농업 정책 수립, 
    소규모 농가 지원, 환경친화적 농업 방식 도입 등을 고려해야 할 것입니다.
    """)

if __name__ == "__main__":
    main()
