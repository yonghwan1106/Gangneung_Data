import pandas as pd
import numpy as np

def load_and_preprocess_data():
    # 데이터 로드
    farm_households_data = pd.read_csv('data/farm_households_data.csv')
    climate_data = pd.read_csv('data/climate_data.csv')
    agricultural_land_data = pd.read_csv('data/agricultural_land_data.csv')
    crop_production_data = pd.read_csv('data/crop_production_data.csv')
    air_quality_data = pd.read_csv('data/air_quality_data.csv')

    # 데이터 전처리
    def preprocess_data(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        return df

    farm_households_data = preprocess_data(farm_households_data)
    climate_data = preprocess_data(climate_data)
    agricultural_land_data = preprocess_data(agricultural_land_data)
    crop_production_data = preprocess_data(crop_production_data)
    air_quality_data = preprocess_data(air_quality_data)

    # 데이터 병합
    merged_data = pd.merge(climate_data, agricultural_land_data, left_index=True, right_index=True)
    merged_data = pd.merge(merged_data, crop_production_data, left_index=True, right_index=True)
    merged_data = pd.merge(merged_data, air_quality_data, left_index=True, right_index=True)

    return merged_data
