import os
import pandas as pd
import numpy as np
import streamlit as st

def load_and_preprocess_data():
    # 프로젝트 루트 디렉토리 경로 얻기
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 데이터 파일 정의
    data_files = {
        'agricultural_land': 'agricultural_land_data.xls',
        'air_quality': 'air_quality_data.xls',
        'climate': 'climate_data.xls',
        'crop_production': 'crop_production_data.xls',
        'farm_households': 'farm_households_data.xls'
    }

    dataframes = {}

    # 데이터 로드
    for key, filename in data_files.items():
        file_path = os.path.join(project_root, 'data', filename)
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            dataframes[key] = df
            st.success(f"Successfully loaded {filename}")
        except Exception as e:
            st.error(f"Error loading {filename}: {str(e)}")
            return None

    # 데이터 전처리
    for key, df in dataframes.items():
        # Year 컬럼을 인덱스로 설정
        if 'Year' in df.columns:
            df['Year'] = pd.to_datetime(df['Year'].astype(str), format='%Y', errors='coerce')
            df.set_index('Year', inplace=True)
        elif 'year' in df.columns:
            df['year'] = pd.to_datetime(df['year'].astype(str), format='%Y', errors='coerce')
            df.set_index('year', inplace=True)

        # 숫자형으로 변환
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 데이터 병합
    merged_data = pd.concat(dataframes.values(), axis=1)

    # 중복 열 제거
    merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    if data is not None:
        print("Final merged data structure:")
        print(data.info())
        print("\nFirst few rows of merged data:")
        print(data.head())
    else:
        print("데이터 로딩에 실패했습니다.")
