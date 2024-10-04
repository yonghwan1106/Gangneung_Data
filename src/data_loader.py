import os
import pandas as pd
import numpy as np
import streamlit as st

# 프로젝트 루트 디렉토리 경로 얻기
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_and_preprocess_data():
    # 데이터 파일 정의
    data_files = {
        'agricultural_land_data': 'agricultural_land_data.csv',
        'air_quality_data': 'air_quality_data.csv',
        'climate_data': 'climate_data.csv',
        'crop_production_data': 'crop_production_data.csv',
        'farm_households_data': 'farm_households_data.csv'
    }

    dataframes = {}

    # 데이터 로드 및 구조 출력
    for key, filename in data_files.items():
        file_path = os.path.join(project_root, 'data', filename)
        try:
            df = pd.read_csv(file_path)
            st.write(f"Columns in {filename}:")
            st.write(df.columns)
            st.write(f"First few rows of {filename}:")
            st.write(df.head())
            st.write("\n")
            dataframes[key] = df
        except Exception as e:
            st.error(f"Error loading {filename}: {str(e)}")
            return None

    # 데이터 전처리
    def preprocess_data(df):
        if 'Year' in df.columns:
            df['Year'] = pd.to_datetime(df['Year'], format='%Y', errors='coerce')
            df.set_index('Year', inplace=True)
        elif 'year' in df.columns:  # 소문자 'year'인 경우
            df['year'] = pd.to_datetime(df['year'], format='%Y', errors='coerce')
            df.set_index('year', inplace=True)
        return df

    # 각 데이터프레임 전처리
    for key in dataframes:
        dataframes[key] = preprocess_data(dataframes[key])

    # 콤마 제거 및 숫자형으로 변환
    for df in dataframes.values():
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')

    # 데이터 병합
    merged_data = pd.concat(dataframes.values(), axis=1)

    # 중복 열 제거
    merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

    # 결측치 확인
    missing_data = merged_data.isnull().sum()
    if missing_data.sum() > 0:
        st.warning("다음 열에서 결측치가 발견되었습니다:")
        st.write(missing_data[missing_data > 0])

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    if data is not None:
        st.write("Final merged data structure:")
        st.write(data.info())
        st.write("\nFirst few rows of merged data:")
        st.write(data.head())
    else:
        st.error("데이터 로딩에 실패했습니다.")
