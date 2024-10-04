import pandas as pd
import numpy as np
import os


def load_and_preprocess_data():
    data_dir = 'data'
    data_files = {
        'farm_households_agricultural_land': 'farm_households_agricultural_land_data.pdf',
        'climate': 'climate_data.pdf',
        'air_quality': 'air_quality_data.pdf',
        'crop_production': 'crop_production_data.pdf',
    }
    

    # 결측치 처리
    merged_data = merged_data.fillna(method='ffill').fillna(method='bfill')

    # 중복된 열 이름 다시 처리
    merged_data.columns = list(dedup_columns(merged_data.columns))

    print("Final merged data columns:", merged_data.columns.tolist())
    print("Final merged data types:", merged_data.dtypes)
    print("Final merged data first few rows:")
    print(merged_data.head())

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    print(data.shape)
