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

def dedup_columns(columns):
    seen = set()
    for c in columns:
        if c in seen:
            i = 1
            while f"{c}_{i}" in seen:
                i += 1
            c = f"{c}_{i}"
        seen.add(c)
        yield c

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
            # 열 이름 표준화
            df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
            
            # 중복된 열 이름 처리
            df.columns = list(dedup_columns(df.columns))
            
            # 첫 번째 열을 연도로 가정하고 처리
            year_col = df.columns[0]
            df[year_col] = safe_to_datetime(df[year_col])
            df.set_index(year_col, inplace=True)
            
            dataframes[key] = df
            
            print(f"{key} data columns:", df.columns.tolist())
            print(f"{key} data types:", df.dtypes)
            print(f"{key} first few rows:")
            print(df.head())
            print("\n")

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
