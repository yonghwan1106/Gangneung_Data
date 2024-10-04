from src.data_loader import load_and_preprocess_data
from src.climate_analysis import analyze_climate
from src.agriculture_structure_analysis import analyze_agriculture_structure
from src.correlation_regression_analysis import perform_correlation_regression_analysis
from src.time_series_analysis import perform_time_series_analysis
from src.machine_learning_models import apply_machine_learning_models

def main():
    # 데이터 로드 및 전처리
    data = load_and_preprocess_data()
    
    # 기후 변화 분석
    analyze_climate(data)
    
    # 농업 구조 변화 분석
    analyze_agriculture_structure(data)
    
    # 상관관계 및 회귀분석
    perform_correlation_regression_analysis(data)
    
    # 시계열 분석
    perform_time_series_analysis(data)
    
    # 머신러닝 모델 적용
    apply_machine_learning_models(data)

if __name__ == "__main__":
    main()
