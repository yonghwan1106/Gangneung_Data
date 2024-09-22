import matplotlib.pyplot as plt

def analyze_agriculture_structure(merged_data):
    # 농가 수 및 농가인구 변화
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.index, merged_data['Farm_Households'], label='Farm Households')
    plt.plot(merged_data.index, merged_data['Farm_Population'], label='Farm Population')
    plt.title('Changes in Farm Households and Population')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.legend()
    plt.show()

    # 경지면적 변화
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.index, merged_data['Total_Cultivated_Area'], label='Total')
    plt.plot(merged_data.index, merged_data['Paddy_Field_Area'], label='Paddy Field')
    plt.plot(merged_data.index, merged_data['Upland_Area'], label='Upland')
    plt.title('Changes in Cultivated Area')
    plt.xlabel('Year')
    plt.ylabel('Area (ha)')
    plt.legend()
    plt.show()

    # 여기에 추가적인 농업 구조 분석 코드를 넣을 수 있습니다.
    # 예: 농가 유형 변화, 농업 생산성 변화 등

    print("Agriculture structure analysis completed.")