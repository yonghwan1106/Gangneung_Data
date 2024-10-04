import os
import pandas as pd
import numpy as np

# 프로젝트 루트 디렉토리 경로 얻기
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_and_preprocess_data():
    # 데이터 로드
    agricultural_land_data = pd.read_csv(os.path.join(project_root, 'data', 'agricultural_land_data.csv'))
    air_quality_data = pd.read_csv(os.path.join(project_root, 'data', 'air_quality_data.csv'))
    climate_data = pd.read_csv(os.path.join(project_root, 'data', 'climate_data.csv'))
    crop_production_data = pd.read_csv(os.path.join(project_root, 'data', 'crop_production_data.csv'))
    farm_households_data = pd.read_csv(os.path.join(project_root, 'data', 'farm_households_data.csv'))


    # 데이터 전처리
    def preprocess_data(df):
        df['Year'] = pd.to_datetime(df['Year'], format='%Y')
        df.set_index('Year', inplace=True)
        return df

    # 각 데이터프레임 전처리
    agricultural_land_data = preprocess_data(agricultural_land_data)
    air_quality_data = preprocess_data(air_quality_data)
    climate_data = preprocess_data(climate_data)
    crop_production_data = preprocess_data(crop_production_data)
    farm_households_data = preprocess_data(farm_households_data)

    # 콤마 제거 및 숫자형으로 변환
    for df in [agricultural_land_data, air_quality_data, climate_data, crop_production_data, farm_households_data]:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.replace(',', '').astype(float)

    # 데이터 병합
    merged_data = pd.concat([
        agricultural_land_data,
        air_quality_data,
        climate_data,
        crop_production_data,
        farm_households_data
    ], axis=1)

    # 중복 열 제거
    merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    print(data.head())
    print(data.columns)
