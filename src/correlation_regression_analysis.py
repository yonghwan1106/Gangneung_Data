import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def run_analysis(merged_data):
    st.title("상관 및 회귀 분석")
    perform_correlation_regression_analysis(merged_data)

def perform_correlation_regression_analysis(merged_data):
    # 상관관계 분석
    st.subheader("상관관계 분석")
    correlation_matrix = merged_data[['temperature', 'precipitation', 'Farmhouseholds', 'PaddyField+Upland', 'RiceProduction', 'PotatoesProduction']].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    # 다중회귀분석 (미곡생산량)
    st.subheader("다중회귀분석 (미곡생산량)")
    X = merged_data[['precipitation', 'temperature', 'Farmhouseholds ', 'Total']]
    y = merged_data['RiceProduction']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    st.write(f'Rice Production - R-squared: {r2:.4f}')
    st.write('Coefficients:')
    for feature, coef in zip(X.columns, model.coef_):
        st.write(f'{feature}: {coef:.4f}')

    # 단순회귀분석 (서류생산량)
    st.subheader("단순회귀분석 (서류생산량)")
    X = merged_data[['precipitation']]
    y = merged_data['PotatoesProduction']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    st.write(f'Potato Production - R-squared: {r2:.4f}')
    st.write(f'Coefficient: {model.coef_[0]:.4f}')

    st.success("Correlation and regression analysis completed.")
