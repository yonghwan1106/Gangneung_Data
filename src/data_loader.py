import pandas as pd
import numpy as np
import os

def safe_read_csv(file_path):
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding='ISO-8859-1')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

def safe_to_datetime(series, format='%Y'):
    try:
        return pd.to_datetime(series, format=format, errors='coerce')
    except Exception as e:
        print(f"Error converting to datetime: {e}")
        return pd.Series(dtype='datetime64[ns]')

def load_and_preprocess_data():
    data_dir = 'data'
    data_files = {
        'farm_households': 'farm_households_data.csv',
        'climate': 'climate_data.csv',
        'air_quality': 'air_quality_data.csv',
        'crop_production': 'crop_production_data.csv',
        'agricultural_land': 'agricultural_land_data.csv'
    }
    
    dataframes = {}
    for key, filename in data_files.items():
        file_path = os.path.join(data_dir, filename)
        df = safe_read_csv(file_path)
        if not df.empty:
            print(f"{key} data columns:", df.columns.tolist())
            dataframes[key] = df

    # 연도 처리 및 인덱스 설정
    for key, df in dataframes.items():
        year_col = df.columns[0]  # 첫 번째 열을 연도 열로 가정
        dataframes[key][year_col] = safe_to_datetime(df[year_col])
        dataframes[key].set_index(year_col, inplace=True)
        print(f"{key} index:", dataframes[key].index.tolist())

    # 공통 인덱스 찾기
    common_index = pd.Index(set.intersection(*[set(df.index) for df in dataframes.values()]))
    print("Common index:", common_index.tolist())

    # 공통 인덱스로 데이터프레임 필터링
    for key in dataframes:
        dataframes[key] = dataframes[key].loc[common_index]

    # 데이터 병합
    merged_data = pd.concat(dataframes.values(), axis=1)

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
    if 'full-time' in merged_data.columns and 'farm_households' in merged_data.columns:
        merged_data['full_time_ratio'] = merged_data['full-time'] / merged_data['farm_households']
        merged_data['part_time_ratio'] = merged_data['part-time'] / merged_data['farm_households']

    # 농업 생산성 계산
    if 'total_production' in merged_data.columns and 'total_cultivated_area' in merged_data.columns:
        merged_data['productivity'] = merged_data['total_production'] / merged_data['total_cultivated_area']

    print("Data loaded and preprocessed successfully.")
    print("Columns in the merged dataset:", merged_data.columns.tolist())
    return merged_data

# 테스트 코드
if __name__ == "__main__":
    data = load_and_preprocess_data()
    print("Columns in the dataset:")
    print(data.columns.tolist())
    print("\nFirst few rows of the data:")
    print(data.head())
    print("\nShape of the data:", data.shape)
