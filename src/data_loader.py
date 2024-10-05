import os
import pandas as pd
import numpy as np
import streamlit as st

def load_and_preprocess_data():
    # 가능한 데이터 디렉토리 경로들
    possible_data_dirs = [
        os.path.join(os.getcwd(), 'data'),
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data'),
        '/mount/src/gangneung-agriculture-climate-analysis',
        '/mount/src/gangneung-agriculture-climate-analysis/data'
    ]
    
    # 데이터 파일 정의
    data_files = {
        'agricultural_land': 'agricultural_land_data.csv',
        'air_quality': 'air_quality_data.csv',
        'climate': 'climate_data.csv',
        'crop_production': 'crop_production_data.csv',
        'farm_households': 'farm_households_data.csv'
    }

    dataframes = {}

    # 데이터 로드
    for key, filename in data_files.items():
        file_found = False
        for data_dir in possible_data_dirs:
            file_path = os.path.join(data_dir, filename)
            if os.path.exists(file_path):
                try:
                    df = pd.read_csv(file_path)
                    dataframes[key] = df
                    file_found = True
                    st.success(f"Successfully loaded {filename}")
                    break
                except Exception as e:
                    st.error(f"Error loading {filename}: {str(e)}")
        if not file_found:
            st.error(f"Could not find {filename} in any of the expected locations")
            return None

    # 데이터 전처리
    for key, df in dataframes.items():
        # Year 컬럼을 인덱스로 설정
        if 'Year' in df.columns:
            df['Year'] = df['Year'].astype(str).str.extract('(\d{4})').astype(int)
            df.set_index('Year', inplace=True)
        elif 'year' in df.columns:
            df['year'] = df['year'].astype(str).str.extract('(\d{4})').astype(int)
            df.set_index('year', inplace=True)

        # 쉼표 제거 및 숫자형으로 변환
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')

    # 데이터 병합
    merged_data = pd.concat(dataframes.values(), axis=1)

    # 중복 열 제거
    merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

    # 인덱스를 datetime으로 변환
    merged_data.index = pd.to_datetime(merged_data.index, format='%Y')

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
