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