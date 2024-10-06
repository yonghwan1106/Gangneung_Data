import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def display_advanced_analysis(data):
    st.header("고급 분석")

    # 5.1 강릉시 기후-농업 연계 지수(CALI) 추이
    st.subheader("5.1 강릉시 기후-농업 연계 지수(CALI) 추이")
    fig = go.Figure(data=go.Scatter(x=data['Year_Display'], y=data['CALI'], mode='lines+markers'))
    fig.update_layout(title="강릉시 기후-농업 연계 지수(CALI) 추이", xaxis_title="연도", yaxis_title="CALI")
    st.plotly_chart(fig)

    # 5.2 강릉시 농업 회복력 평가 매트릭스(ARAM) 레이더 차트
    st.subheader("5.2 강릉시 농업 회복력 평가 매트릭스(ARAM) 레이더 차트")
    categories = ['작물 다양성', '관개 시스템 효율성', '농가 경제력', '기술 적용도', '정책 지원 수준']
    fig = go.Figure(data=go.Scatterpolar(
      r=[3, 4, 2, 3, 4],
      theta=categories,
      fill='toself'
    ))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 5]
        )),
      showlegend=False
    )
    st.plotly_chart(fig)

    # 5.3 강릉시 농업-기후 모니터링 대시보드
    st.subheader("5.3 강릉시 농업-기후 모니터링 대시보드")
    fig = make_subplots(rows=2, cols=2)
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['temperature'], name="평균 기온"), row=1, col=1)
    fig.add_trace(go.Bar(x=data['Year_Display'], y=data['precipitation'], name="강수량"), row=1, col=2)
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['RiceProduction'], name="미곡 생산량"), row=2, col=1)
    fig.add_trace(go.Scatter(x=data['Year_Display'], y=data['PotatoesProduction'], name="서류 생산량"), row=2, col=2)
    fig.update_layout(height=600, width=800, title_text="강릉시 농업-기후 모니터링 대시보드")
    st.plotly_chart(fig)

    # 5.4 농가 협동 체계 구축 단계별 접근
    st.subheader("5.4 농가 협동 체계 구축 단계별 접근")
    stages = ['1년차', '2년차', '3년차', '4년차', '5년차']
    participants = [20, 50, 100, 200, 300]
    productivity = [5, 10, 15, 20, 25]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=stages, y=participants, name="참여 농가 수"), secondary_y=False)
    fig.add_trace(go.Scatter(x=stages, y=productivity, name="생산성 향상률 (%)"), secondary_y=True)
    fig.update_layout(title_text="농가 협동 체계 구축 단계별 접근")
    fig.update_xaxes(title_text="단계")
    fig.update_yaxes(title_text="참여 농가 수", secondary_y=False)
    fig.update_yaxes(title_text="생산성 향상률 (%)", secondary_y=True)
    st.plotly_chart(fig)

    # 5.5 농업 회복력 개선 효과
    st.subheader("5.5 농업 회복력 개선 효과")
    categories = ['생산 안정성', '자연재해 대응', '수자원 관리', '병해충 관리', '품질 향상']
    current = [65, 70, 60, 75, 80]
    expected = [90, 85, 88, 92, 95]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=current,
          theta=categories,
          fill='toself',
          name='현재'
    ))
    fig.add_trace(go.Scatterpolar(
          r=expected,
          theta=categories,
          fill='toself',
          name='기대효과'
    ))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 100]
        )),
      showlegend=True
    )
    st.plotly_chart(fig)

    # 5.6 스마트팜 기술 도입 예상 효과
    st.subheader("5.6 스마트팜 기술 도입 예상 효과")
    years = [2024, 2025, 2026, 2027, 2028]
    adoption = [5, 15, 30, 50, 70]
    productivity = [100, 110, 125, 140, 160]
    cost = [100, 95, 90, 85, 80]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=adoption, mode='lines+markers', name='스마트팜 도입률 (%)'))
    fig.add_trace(go.Scatter(x=years, y=productivity, mode='lines+markers', name='생산성 지수'))
    fig.add_trace(go.Scatter(x=years, y=cost, mode='lines+markers', name='생산 비용 지수'))
    fig.update_layout(title="스마트팜 기술 도입 예상 효과", xaxis_title="연도", yaxis_title="지수")
    st.plotly_chart(fig)

    # 5.7 작물별 맞춤형 재배 가이드라인 구현 로드맵
    st.subheader("5.7 작물별 맞춤형 재배 가이드라인 구현 로드맵")
    stages = ['기획 및 팀 구성', '데이터 수집 및 모델 개발', '시스템 구축 및 시범 운영', '전면 도입 및 지속적 개선']
    start = ['2024-01-01', '2024-04-01', '2024-10-01', '2025-04-01']
    end = ['2024-03-31', '2024-09-30', '2025-03-31', '2025-12-31']
    fig = go.Figure([go.Bar(
        x=[3, 6, 6, 9],
        y=stages,
        orientation='h'
    )])
    fig.update_layout(title="작물별 맞춤형 재배 가이드라인 구현 로드맵",
                      xaxis_title="개월",
                      yaxis_title="단계")
    st.plotly_chart(fig)
