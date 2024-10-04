import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st

def run_analysis(merged_data):
    st.title("Agriculture Structure Analysis")

    # 농가 수 및 농가인구 변화
    st.subheader("Changes in Farm Households and Population")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['Farm_Households'], label='Farm Households')
    ax.plot(merged_data.index, merged_data['Farm_Population'], label='Farm Population')
    ax.set_title('Changes in Farm Households and Population')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number')
    ax.legend()
    st.pyplot(fig)

    # 경지면적 변화
    st.subheader("Changes in Cultivated Area")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['Total_Cultivated_Area'], label='Total')
    ax.plot(merged_data.index, merged_data['Paddy_Field_Area'], label='Paddy Field')
    ax.plot(merged_data.index, merged_data['Upland_Area'], label='Upland')
    ax.set_title('Changes in Cultivated Area')
    ax.set_xlabel('Year')
    ax.set_ylabel('Area (ha)')
    ax.legend()
    st.pyplot(fig)

    # 농가 유형 변화 (전업농 vs 겸업농)
    st.subheader("Changes in Farm Type Ratio")
    merged_data['Full_time_ratio'] = merged_data['Full_time_farm'] / merged_data['Farm_Households']
    merged_data['Part_time_ratio'] = merged_data['Part_time_farm'] / merged_data['Farm_Households']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.stackplot(merged_data.index, merged_data['Full_time_ratio'], merged_data['Part_time_ratio'], 
                 labels=['Full-time', 'Part-time'])
    ax.set_title('Changes in Farm Type Ratio')
    ax.set_xlabel('Year')
    ax.set_ylabel('Ratio')
    ax.legend(loc='upper left')
    st.pyplot(fig)

    # 농업 생산성 변화
    st.subheader("Changes in Agricultural Productivity")
    merged_data['Productivity'] = merged_data['Total_Production'] / merged_data['Total_Cultivated_Area']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(merged_data.index, merged_data['Productivity'])
    ax.set_title('Changes in Agricultural Productivity')
    ax.set_xlabel('Year')
    ax.set_ylabel('Production per hectare')
    st.pyplot(fig)

    st.success("Agriculture structure analysis completed.")
