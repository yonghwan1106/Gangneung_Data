# correlation_regression_analysis.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_data():
    # 데이터 로드 (실제 경로에 맞게 수정 필요)
    data = pd.read_csv('../data/total_data.csv')
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')
    data.set_index('Year', inplace=True)
    return data

def rainfall_crop_relation(data):
    st.subheader("3.1 강수량과 주요 작물 생산량의 관계")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=data.index, y=data['precipitation'], name="강수량 (mm)"),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=data.index, y=data['RiceProduction'], name="미곡 생산량 (톤)"),
        secondary_y=True,
    )
    
    fig.add_trace(
        go.Scatter(x=data.index, y=data['PotatoesProduction'], name="서류 생산량 (톤)"),
        secondary_y=True,
    )
    
    fig.update_layout(title_text="강수량과 주요 작물 생산량의 관계")
    fig.update_xaxes(title_text="연도")
    fig.update_yaxes(title_text="강수량 (mm)", secondary_y=False)
    fig.update_yaxes(title_text="생산량 (톤)", secondary_y=True)
    
    st.plotly_chart(fig)

def farm_type_change(data):
    st.subheader("3.2 농가유형의 변화: 전업농 및 겸업농 비율 변화")
    
    fig = go.Figure(data=[
        go.Bar(name='전업농 비율 (%)', x=data.index, y=data['fullTimeFarmRatio']),
        go.Bar(name='겸업농 비율 (%)', x=data.index, y=data['partTimeFarmRatio'])
    ])
    
    fig.update_layout(barmode='stack', title_text='전업농 및 겸업농 비율 변화')
    fig.update_xaxes(title_text="연도")
    fig.update_yaxes(title_text="비율 (%)")
    
    st.plotly_chart(fig)

def env_agri_relation(data):
    st.subheader("3.3 환경 요인과 농업 생산의 관계")
    
    fig = go.Figure(data=go.Scatter(
        x=data['PM10'],
        y=data['RiceProduction'],
        mode='markers',
        marker=dict(size=10),
        text=data.index.year  # 마커에 연도 표시
    ))
    
    fig.update_layout(title='PM10과 미곡 생산량의 관계')
    fig.update_xaxes(title_text="PM10 (μg/m³)")
    fig.update_yaxes(title_text="미곡 생산량 (톤)")
    
    st.plotly_chart(fig)

def run_analysis(data):
    st.title("상관 분석 및 회귀 분석")
    
    rainfall_crop_relation(data)
    farm_type_change(data)
    env_agri_relation(data)

if __name__ == "__main__":
    data = load_data()
    run_analysis(data)
