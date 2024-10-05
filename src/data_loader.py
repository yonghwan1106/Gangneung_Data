import os
import pandas as pd
import streamlit as st

def load_and_preprocess_data():
    # 프로젝트 루트 디렉토리 경로 얻기
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 데이터 파일 경로
    file_path = os.path.join(project_root, 'data', 'total_data.csv')

    try:
        # CSV 파일 읽기
        df = pd.read_csv(file_path)
        
        # Year 열을 datetime 형식으로 변환하고 인덱스로 설정
        df['Year'] = pd.to_datetime(df['Year'], format='%Y')
        df.set_index('Year', inplace=True)
        
        # 쉼표가 포함된 숫자 열 처리
        numeric_columns = ['PaddyField+Upland', 'PaddyField', 'Upland', 'Farmhouseholds ', 'Farmpopulation', 
                           'RiceProduction', 'PotatoesProduction', 'precipitation']
        for col in numeric_columns:
            df[col] = df[col].str.replace(',', '').astype(float)

        st.success("데이터를 성공적으로 로드했습니다.")
        return df

    except Exception as e:
        st.error(f"데이터 로딩 중 오류가 발생했습니다: {str(e)}")
        return None

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    if data is not None:
        print("로드된 데이터 구조:")
        print(data.info())
        print("\n데이터 샘플:")
        print(data.head())
    else:
        print("데이터 로딩에 실패했습니다.")
