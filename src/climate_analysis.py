import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def analyze_climate(merged_data):
    # 연간 평균 기온 추이
    plt.figure(figsize=(12, 6))
    yearly_temp = merged_data.resample('Y')['Temperature'].mean()
    plt.plot(yearly_temp.index.year, yearly_temp.values)
    plt.title('Annual Average Temperature Trend')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.savefig('results/annual_temperature_trend.png')
    plt.close()

    # 연간 강수량 변화
    plt.figure(figsize=(12, 6))
    yearly_precip = merged_data.resample('Y')['Precipitation'].sum()
    plt.bar(yearly_precip.index.year, yearly_precip.values)
    plt.title('Annual Precipitation')
    plt.xlabel('Year')
    plt.ylabel('Precipitation (mm)')
    plt.savefig('results/annual_precipitation.png')
    plt.close()

    # 계절별 평균 기온 변화
    merged_data['Season'] = pd.to_datetime(merged_data.index).month.map({1:'Winter', 2:'Winter', 3:'Spring', 
                                                                         4:'Spring', 5:'Spring', 6:'Summer',
                                                                         7:'Summer', 8:'Summer', 9:'Fall',
                                                                         10:'Fall', 11:'Fall', 12:'Winter'})
    seasonal_temp = merged_data.groupby(['Season', merged_data.index.year])['Temperature'].mean().unstack()
    plt.figure(figsize=(12, 6))
    sns.heatmap(seasonal_temp, cmap='YlOrRd', annot=True)
    plt.title('Seasonal Average Temperature')
    plt.savefig('results/seasonal_temperature.png')
    plt.close()

    # 극한 기후 현상 분석
    extreme_temp = merged_data[merged_data['Temperature'] > merged_data['Temperature'].quantile(0.95)]
    plt.figure(figsize=(12, 6))
    plt.scatter(extreme_temp.index, extreme_temp['Temperature'])
    plt.title('Extreme Temperature Events')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.savefig('results/extreme_temperature_events.png')
    plt.close()

    print("Climate analysis completed.")
