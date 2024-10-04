import os
import pandas as pd
import numpy as np

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
        df = pd.read_csv(file_path)
        print(f"Columns in {filename}:")
        print(df.columns)
        print(f"First few rows of {filename}:")
        print(df.head())
        print("\n")
        dataframes[key] = df

    # 데이터 전처리
    def preprocess_data(df):
        if 'Year' in df.columns:
            df['Year'] = pd.to_datetime(df['Year'], format='%Y')
            df.set_index('Year', inplace=True)
        elif 'year' in df.columns:  # 소문자 'year'인 경우
            df['year'] = pd.to_datetime(df['year'], format='%Y')
            df.set_index('year', inplace=True)
        return df

    # 각 데이터프레임 전처리
    for key in dataframes:
        dataframes[key] = preprocess_data(dataframes[key])

    # 콤마 제거 및 숫자형으로 변환
    for df in dataframes.values():
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.replace(',', '').astype(float)

    # 데이터 병합
    merged_data = pd.concat(dataframes.values(), axis=1)

    # 중복 열 제거
    merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    print("Final merged data structure:")
    print(data.info())
    print("\nFirst few rows of merged data:")
    print(data.head())
