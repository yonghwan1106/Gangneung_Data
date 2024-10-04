import pandas as pd
import numpy as np

def load_and_preprocess_data():
    # 데이터 로드
    climate_data = pd.read_csv('data/climate_data.csv')
    print("Climate data columns:", climate_data.columns)
    agriculture_data = pd.read_csv('data/agriculture_data.csv')
    crop_production_data = pd.read_csv('data/crop_production_data.csv')
    air_quality_data = pd.read_csv('data/air_quality_data.txt')

    # 데이터 전처리
    def preprocess_data(df):
        if 'Year' in df.columns:
            df['Date'] = pd.to_datetime(df['Year'], format='%Y')
        elif 'Date' not in df.columns:
            df['Date'] = pd.to_datetime(df.index)
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
