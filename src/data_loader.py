import pandas as pd
import tabula
import numpy as np
from datetime import datetime

def load_farm_households_and_land_data():
    tables = tabula.read_pdf("farm_households_agricultural_land_data.pdf", pages='all')
    
    # 농가 및 농가인구 데이터
    farm_households = tables[0]
    farm_households.columns = ['Year', 'Total_Households', 'Full_time_farm', 'Part_time_farm', 
                               'Total_Population', 'Male_Population', 'Female_Population']
    farm_households['Year'] = farm_households['Year'].astype(int)
    
    # 경지면적 데이터
    agricultural_land = tables[1]
    agricultural_land.columns = ['Year', 'Total_Area', 'Paddy_Field_Area', 'Upland_Area', 
                                 'Total_Area_per_Household', 'Paddy_Field_per_Household', 'Upland_per_Household']
    agricultural_land['Year'] = agricultural_land['Year'].astype(int)
    
    # 두 데이터프레임 병합
    merged_data = pd.merge(farm_households, agricultural_land, on='Year', how='outer')
    return merged_data

def load_crop_production_data():
    df = tabula.read_pdf("crop_production_data.pdf", pages='all')[0]
    df.columns = ['Year', 'Total_Area', 'Total_Production', 'Rice_Area', 'Rice_Production',
                  'Barley_Area', 'Barley_Production', 'Misc_Grains_Area', 'Misc_Grains_Production',
                  'Beans_Area', 'Beans_Production', 'Potato_Area', 'Potato_Production']
    df['Year'] = df['Year'].astype(int)
    return df

def load_climate_data():
    df = tabula.read_pdf("climate_data.pdf", pages='all')[0]
    df.columns = ['Year'] + [f'Precipitation_{month}' for month in range(1, 13)] + ['Total_Precipitation']
    df['Year'] = df['Year'].astype(int)
    return df

def load_air_quality_data():
    df = tabula.read_pdf("air_quality_data.pdf", pages='all')[0]
    df.columns = ['Year', 'SO2', 'CO', 'NO2', 'PM10', 'PM25', 'O3']
    df['Year'] = df['Year'].astype(int)
    return df

def preprocess_data():
    farm_households_and_land = load_farm_households_and_land_data()
    crop_production = load_crop_production_data()
    climate = load_climate_data()
    air_quality = load_air_quality_data()

    # Merge all dataframes
    merged_data = farm_households_and_land.merge(crop_production, on='Year', how='outer')
    merged_data = merged_data.merge(climate, on='Year', how='outer')
    merged_data = merged_data.merge(air_quality, on='Year', how='outer')

    # Create date index
    merged_data['Date'] = pd.to_datetime(merged_data['Year'].astype(str) + '-12-31')
    merged_data.set_index('Date', inplace=True)

    # Calculate average temperature (placeholder as we don't have temperature data)
    merged_data['Temperature'] = np.random.uniform(10, 20, len(merged_data))  # Placeholder

    return merged_data

def load_and_preprocess_data():
    return preprocess_data()

if __name__ == "__main__":
    data = load_and_preprocess_data()
    print(data.head())
    print(data.columns)
