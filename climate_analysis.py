import matplotlib.pyplot as plt

def analyze_climate(merged_data):
    # 연간 평균 기온 추이
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.resample('Y')['Temperature'].mean())
    plt.title('Annual Average Temperature Trend')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.show()

    # 연간 강수량 변화
    plt.figure(figsize=(12, 6))
    plt.bar(merged_data.resample('Y').index.year, merged_data.resample('Y')['Precipitation'].sum())
    plt.title('Annual Precipitation')
    plt.xlabel('Year')
    plt.ylabel('Precipitation (mm)')
    plt.show()

    # 여기에 추가적인 기후 분석 코드를 넣을 수 있습니다.
    # 예: 계절별 분석, 극한 기후 현상 분석 등

    print("Climate analysis completed.")