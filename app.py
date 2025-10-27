import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained pipeline + model
# -----------------------------
preprocessor = joblib.load("preprocessing_pipeline.joblib")
model = joblib.load("best_model.joblib")

st.title("🏠 California Housing Price Prediction App")
st.write("Enter the details below to predict median house value.")

# -----------------------------
# User Inputs
# -----------------------------
longitude = st.number_input("Longitude", -125.0, -114.0, -120.0)
latitude = st.number_input("Latitude", 32.0, 42.0, 37.0)
housing_median_age = st.number_input("Housing Median Age", 1.0, 52.0, 20.0)
total_rooms = st.number_input("Total Rooms", 1.0, 50000.0, 2000.0)
total_bedrooms = st.number_input("Total Bedrooms", 1.0, 10000.0, 400.0)
population = st.number_input("Population", 1.0, 50000.0, 1000.0)
households = st.number_input("Households", 1.0, 10000.0, 300.0)
median_income = st.number_input("Median Income", 0.0, 15.0, 4.0)
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

# -----------------------------
# Create input DataFrame
# -----------------------------
input_df = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean_proximity]
})

# -----------------------------
# Derived / Engineered Features
# -----------------------------
input_df["rooms_per_household"] = input_df["total_rooms"] / input_df["households"]
input_df["bedrooms_per_room"] = input_df["total_bedrooms"] / input_df["total_rooms"]
input_df["population_per_household"] = input_df["population"] / input_df["households"]

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict House Price"):
    try:
        X_prepared = preprocessor.transform(input_df)
        prediction = model.predict(X_prepared)
        st.success(f"🏡 **Predicted Median House Value:** ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built by Waqas Gurmani | California Housing ML Project")
