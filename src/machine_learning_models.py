import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import xgboost as xgb

def apply_machine_learning_models(merged_data):
    X = merged_data[['Year', 'Temperature', 'Precipitation', 'Farm_Households', 'Total_Cultivated_Area']]
    y = merged_data['Rice_Production']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 랜덤 포레스트 모델
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)
    print('Random Forest R-squared:', r2_score(y_test, y_pred))

    # 특성 중요도
    feature_importance = pd.DataFrame({'feature': X.columns, 'importance': rf_model.feature_importances_})
    feature_importance = feature_importance.sort_values('importance', ascending=False)
    print("Random Forest Feature Importance:")
    print(feature_importance)

    # XGBoost 모델
    xgb_model = xgb.XGBRegressor(random_state=42)
    xgb_model.fit(X_train, y_train)

    y_pred = xgb_model.predict(X_test)
    print('XGBoost R-squared:', r2_score(y_test, y_pred))

    # 특성 중요도
    feature_importance = pd.DataFrame({'feature': X.columns, 'importance': xgb_model.feature_importances_})
    feature_importance = feature_importance.sort_values('importance', ascending=False)
    print("XGBoost Feature Importance:")
    print(feature_importance)

    print("Machine learning models analysis completed.")
