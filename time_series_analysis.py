import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

def perform_time_series_analysis(merged_data):
    # SARIMA 모델
    model = SARIMAX(merged_data['Rice_Production'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit()

    # 예측
    forecast = results.forecast(steps=36)  # 3년 예측
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data.index, merged_data['Rice_Production'], label='Observed')
    plt.plot(forecast.index, forecast, label='Forecast')
    plt.title('Rice Production Forecast')
    plt.xlabel('Year')
    plt.ylabel('Production (ton)')
    plt.legend()
    plt.show()

    print("Time series analysis completed.")