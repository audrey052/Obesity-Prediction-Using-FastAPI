import streamlit as st
import requests

def main():
    st.set_page_config(page_title="Obesity Prediction")
    st.title("Obesity Prediction App")
    st.markdown("Fill out the following form to predict obesity level based on your data.")

    with st.form("prediction_form"):
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.slider("Age", 1, 55, 22)
        height = st.number_input("Height (in meters)", 1.0, 1.95, 1.65)
        weight = st.number_input("Weight (in kg)", 10.0, 173.0, 55.0)
        family_history = st.selectbox("Family History with Overweight", ["yes", "no"])
        favc = st.selectbox("Frequent Consumption of High Caloric Food (FAVC)", ["yes", "no"])
        fcvc = st.slider("Frequency of Vegetable Consumption (FCVC)", 1, 3, 3)
        ncp = st.slider("Number of Main Meals in a Day (NCP)", 1, 4, 3)
        caec = st.selectbox("Consumption of Food Between Meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
        smoke = st.selectbox("Do you Smoke?", ["yes", "no"])
        ch2o = st.slider("Water Consumption (C2H0)", 1, 3, 2)
        scc = st.selectbox("Do you Monitor your Calories Consumption? (SCC)", ["yes", "no"])
        faf = st.slider("Physical Activity Frequency (FAF)", 0, 3, 1)
        tue = st.slider("Time Spend for Technology (TUE)", 0, 2, 1)
        calc = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"])
        mtrans = st.selectbox("Transportation", ["Public_Transportation", "Walking", "Automobile", "Bike", "Motorbike"])

        submitted = st.form_submit_button("Predict")

    if submitted:
        payload = [{
            "Gender": gender,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "family_history_with_overweight": family_history,
            "FAVC": favc,
            "FCVC": fcvc,
            "NCP": ncp,
            "CAEC": caec,
            "SMOKE": smoke,
            "CH2O": ch2o,
            "SCC": scc,
            "FAF": faf,
            "TUE": tue,
            "CALC": calc,
            "MTRANS": mtrans
        }]

        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()["predictions"][0]

            obesity_labels = {
                0: 'Insufficient_Weight',
                1: 'Normal_Weight',
                2: 'Overweight_Level_I',
                3: 'Overweight_Level_II',
                4: 'Obesity_Type_I',
                5: 'Obesity_Type_II',
                6: 'Obesity_Type_III'
            }
            label = obesity_labels.get(result, "Unknown")
            st.success(f"Predicted Obesity Level: **{label}**")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()
