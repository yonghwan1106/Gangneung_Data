import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import xgboost as xgb

def run_analysis(merged_data):
    st.title("머신러닝 모델 분석")
    apply_machine_learning_models(merged_data)

def apply_machine_learning_models(merged_data):
    X = merged_data[['temperature', 'precipitation', 'Farmhouseholds', 'PaddyField+Upland']]
    y = merged_data['RiceProduction']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 랜덤 포레스트 모델
    st.subheader("랜덤 포레스트 모델")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)
    st.write(f'Random Forest R-squared: {r2_score(y_test, y_pred):.4f}')

    # 특성 중요도
    feature_importance = pd.DataFrame({'feature': X.columns, 'importance': rf_model.feature_importances_})
    feature_importance = feature_importance.sort_values('importance', ascending=False)
    st.write("Random Forest Feature Importance:")
    st.write(feature_importance)

    # XGBoost 모델
    st.subheader("XGBoost 모델")
    xgb_model = xgb.XGBRegressor(random_state=42)
    xgb_model.fit(X_train, y_train)

    y_pred = xgb_model.predict(X_test)
    st.write(f'XGBoost R-squared: {r2_score(y_test, y_pred):.4f}')

    # 특성 중요도
    feature_importance = pd.DataFrame({'feature': X.columns, 'importance': xgb_model.feature_importances_})
    feature_importance = feature_importance.sort_values('importance', ascending=False)
    st.write("XGBoost Feature Importance:")
    st.write(feature_importance)

    st.success("Machine learning models analysis completed.")
