import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def run_analysis(data):
    analyze_agriculture_structure(data)
    
def analyze_agriculture_structure(merged_data):
    # 농가 수 및 농가인구 변화
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.index, merged_data['Farm_Households'], label='Farm Households')
    plt.plot(merged_data.index, merged_data['Farm_Population'], label='Farm Population')
    plt.title('Changes in Farm Households and Population')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.legend()
    plt.savefig('results/farm_households_population.png')
    plt.close()

    # 경지면적 변화
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.index, merged_data['Total_Cultivated_Area'], label='Total')
    plt.plot(merged_data.index, merged_data['Paddy_Field_Area'], label='Paddy Field')
    plt.plot(merged_data.index, merged_data['Upland_Area'], label='Upland')
    plt.title('Changes in Cultivated Area')
    plt.xlabel('Year')
    plt.ylabel('Area (ha)')
    plt.legend()
    plt.savefig('results/cultivated_area_changes.png')
    plt.close()

    # 농가 유형 변화 (전업농 vs 겸업농)
    merged_data['Full_time_ratio'] = merged_data['Full_time_farm'] / merged_data['Farm_Households']
    merged_data['Part_time_ratio'] = merged_data['Part_time_farm'] / merged_data['Farm_Households']
    
    plt.figure(figsize=(12, 6))
    plt.stackplot(merged_data.index, merged_data['Full_time_ratio'], merged_data['Part_time_ratio'], 
                  labels=['Full-time', 'Part-time'])
    plt.title('Changes in Farm Type Ratio')
    plt.xlabel('Year')
    plt.ylabel('Ratio')
    plt.legend(loc='upper left')
    plt.savefig('results/farm_type_ratio.png')
    plt.close()

    # 농업 생산성 변화
    merged_data['Productivity'] = merged_data['Total_Production'] / merged_data['Total_Cultivated_Area']
    
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.index, merged_data['Productivity'])
    plt.title('Changes in Agricultural Productivity')
    plt.xlabel('Year')
    plt.ylabel('Production per hectare')
    plt.savefig('results/agricultural_productivity.png')
    plt.close()

    print("Agriculture structure analysis completed.")
