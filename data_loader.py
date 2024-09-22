import pandas as pd
import numpy as np

def load_and_preprocess_data():
    # 데이터 로드
    climate_data = pd.read_csv('climate_data.csv')
    agriculture_data = pd.read_csv('agriculture_data.csv')
    crop_production_data = pd.read_csv('crop_production_data.csv')
    air_quality_data = pd.read_csv('air_quality_data.csv')

    # 데이터 전처리
    def preprocess_data(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        return df

    climate_data = preprocess_data(climate_data)
    agriculture_data = preprocess_data(agriculture_data)
    crop_production_data = preprocess_data(crop_production_data)
    air_quality_data = preprocess_data(air_quality_data)

    # 데이터 병합
    merged_data = pd.merge(climate_data, agriculture_data, left_index=True, right_index=True)
    merged_data = pd.merge(merged_data, crop_production_data, left_index=True, right_index=True)
    merged_data = pd.merge(merged_data, air_quality_data, left_index=True, right_index=True)

    return merged_data