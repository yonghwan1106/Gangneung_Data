# 상관관계 분석
correlation_matrix = merged_data[['Temperature', 'Precipitation', 'Farm_Households', 'Total_Cultivated_Area', 'Rice_Production', 'Potato_Production']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 다중회귀분석 (미곡생산량)
X = merged_data[['Precipitation', 'Temperature', 'Farm_Households', 'Total_Cultivated_Area']]
y = merged_data['Rice_Production']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print('R-squared:', r2_score(y_test, y_pred))
print('Coefficients:', model.coef_)

# 단순회귀분석 (서류생산량)
X = merged_data[['Precipitation']]
y = merged_data['Potato_Production']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print('R-squared:', r2_score(y_test, y_pred))
print('Coefficient:', model.coef_[0])