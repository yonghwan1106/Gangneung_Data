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

# 랜덤 포레스트 모델
X = merged_data[['Year', 'Temperature', 'Precipitation', 'Farm_Households', 'Total_Cultivated_Area']]
y = merged_data['Rice_Production']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
print('Random Forest R-squared:', r2_score(y_test, y_pred))

# 특성 중요도
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': rf_model.feature_importances_})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print(feature_importance)

# XGBoost 모델
xgb_model = xgb.XGBRegressor(random_state=42)
xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)
print('XGBoost R-squared:', r2_score(y_test, y_pred))

# 특성 중요도
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': xgb_model.feature_importances_})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print(feature_importance)