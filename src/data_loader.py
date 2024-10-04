import pandas as pd
import numpy as np

def load_and_preprocess_data():
    # 데이터 로드
    farm_households_data = pd.read_csv('data/farm_households_data.csv', encoding='utf-8')
    climate_data = pd.read_csv('data/climate_data.csv', encoding='utf-8')
    air_quality_data = pd.read_csv('data/air_quality_data.csv', encoding='utf-8')
    crop_production_data = pd.read_csv('data/crop_production_data.csv', encoding='utf-8')
    agricultural_land_data = pd.read_csv('data/agricultural_land_data.csv', encoding='utf-8')

    # 데이터 확인 및 열 이름 출력
    print("Climate data columns:", climate_data.columns.tolist())
    
    # 연도 처리 (실제 열 이름에 맞게 수정)
    farm_households_data['Year'] = pd.to_datetime(farm_households_data['Year'].astype(str).str.strip(), format='%Y', errors='coerce')
    climate_data['Year'] = pd.to_datetime(climate_data.iloc[:, 0], format='%Y')  # 첫 번째 열을 Year로 가정
    air_quality_data['year'] = pd.to_datetime(air_quality_data['year'], format='%Y')
    crop_production_data['year'] = pd.to_datetime(crop_production_data['year'], format='%Y')
    agricultural_land_data['Year'] = pd.to_datetime(agricultural_land_data['Year'], format='%Y')

    # 인덱스 설정 (실제 열 이름에 맞게 수정)
    farm_households_data.set_index('Year', inplace=True)
    climate_data.set_index(climate_data.columns[0], inplace=True)
    air_quality_data.set_index('year', inplace=True)
    crop_production_data.set_index('year', inplace=True)
    agricultural_land_data.set_index('Year', inplace=True)

    # 데이터 병합
    merged_data = pd.concat([farm_households_data, climate_data, air_quality_data, 
                             crop_production_data, agricultural_land_data], axis=1)

    # 결측치 처리
    merged_data = merged_data.fillna(method='ffill').fillna(method='bfill')

    # 열 이름 표준화
    merged_data.columns = merged_data.columns.str.strip().str.replace(' ', '_').str.lower()

    # 필요한 열 생성 또는 이름 변경
    column_mapping = {
        'total': 'farm_households',
        'total_x': 'total_cultivated_area',
        'paddy_field': 'paddy_field_area',
        'upland': 'upland_area',
        'total_y': 'total_production'
    }
    merged_data.rename(columns=column_mapping, inplace=True)

    # 농가 유형 비율 계산
    merged_data['full_time_ratio'] = merged_data['full-time'] / merged_data['farm_households']
    merged_data['part_time_ratio'] = merged_data['part-time'] / merged_data['farm_households']

    # 농업 생산성 계산
    merged_data['productivity'] = merged_data['total_production'] / merged_data['total_cultivated_area']

    print("Data loaded and preprocessed successfully.")
    print("Columns in the merged dataset:", merged_data.columns.tolist())

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    print(data.head())
    print(data.shape)
