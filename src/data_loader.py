import pandas as pd
import numpy as np

def load_and_preprocess_data():
    # 데이터 로드
    farm_households_population = pd.read_csv('data/farm_households_and_population_data.csv')
    climate_data = pd.read_csv('data/climate_data.csv')
    air_quality_data = pd.read_csv('data/air_quality_data.csv')
    crop_production_data = pd.read_csv('data/crop_production_data.csv')
    agriculture_data = pd.read_csv('data/agriculture_data.csv')

    # 연도 컬럼 처리 함수
    def process_year_column(df):
        year_columns = ['Year', 'year', 'Date', 'date']
        for col in year_columns:
            if col in df.columns:
                df['Year'] = pd.to_datetime(df[col]).dt.year
                df.set_index('Year', inplace=True)
                break
        return df

    # 각 데이터프레임에 연도 처리 적용
    dataframes = [farm_households_population, climate_data, air_quality_data, 
                  crop_production_data, agriculture_data]
    processed_dfs = [process_year_column(df) for df in dataframes]

    # 데이터 병합
    merged_data = pd.concat(processed_dfs, axis=1, join='outer')

    # 결측치 처리
    merged_data = merged_data.fillna(method='ffill').fillna(method='bfill')

    # 열 이름 표준화
    merged_data.columns = merged_data.columns.str.strip().str.replace(' ', '_').str.lower()

    # 필요한 열 생성 또는 이름 변경
    column_mapping = {
        'farm_households': 'farm_households',
        'farm_population': 'farm_population',
        'total_cultivated_area': 'total_cultivated_area',
        'paddy_field_area': 'paddy_field_area',
        'upland_area': 'upland_area',
        'total_production': 'total_production'
    }
    merged_data.rename(columns=column_mapping, inplace=True)

    # 농가 유형 비율 계산 (만약 해당 데이터가 있다면)
    if 'full_time_farm' in merged_data.columns and 'part_time_farm' in merged_data.columns:
        merged_data['full_time_ratio'] = merged_data['full_time_farm'] / merged_data['farm_households']
        merged_data['part_time_ratio'] = merged_data['part_time_farm'] / merged_data['farm_households']

    # 농업 생산성 계산
    if 'total_production' in merged_data.columns and 'total_cultivated_area' in merged_data.columns:
        merged_data['productivity'] = merged_data['total_production'] / merged_data['total_cultivated_area']

    print("Data loaded and preprocessed successfully.")
    print("Columns in the merged dataset:", merged_data.columns.tolist())

    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    print(data.head())
    print(data.shape)
