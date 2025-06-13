import streamlit as st
import joblib
import pandas as pd
import os
from azure.storage.blob import BlobServiceClient
from datetime import datetime
import json

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "app-data"

def save_to_blob(input_data: dict, output_data: str):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"{timestamp}/"

    container_client.upload_blob(name=f"{folder_name}input.json", data=json.dumps(input_data), overwrite=True)
    container_client.upload_blob(name=f"{folder_name}output.txt", data=str(output_data), overwrite=True)

@st.cache_resource
def load_model():
    model = joblib.load(os.path.join("model", "model.joblib"))
    feature_names = joblib.load(os.path.join("model", "feature_names.joblib"))
    return model, feature_names

def predict_price(model, feature_names, input_data: dict):
    df = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df)

    for col in feature_names:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[feature_names]
    prediction = model.predict(df_encoded)[0]
    return round(prediction, 2)

st.title("Szacowanie ceny mieszkania")

model, feature_names = load_model()

with st.form(key="parametry_mieszkania"):
    st.subheader("Wybierz parametry mieszkania")

    rok_budowy = st.date_input("Wybierz rok budowy").year
    liczba_pokoi = st.select_slider("Liczba pokoi", options=[1,2,3,4,5,6,7,8,9,10])
    pietro = st.number_input("Piętro", min_value=0, max_value=50)
    metraz = st.number_input("Metraż (w metrach kwadratowych)", min_value=20, max_value=500)
    dzielnica = st.selectbox("Dzielnica", [
        "Bemowo", "Białołęka", "Bielany", "Mokotów", "Ochota", 
        "Praga-Południe", "Praga-Północ", "Rembertów", "Śródmieście",
        "Targówek", "Ursus", "Ursynów", "Wawer", "Wesoła", 
        "Wilanów", "Włochy", "Wola", "Żoliborz"
    ])
    wyposazenie = st.selectbox("Wyposażenie", ['Tak', 'Nie'])

    pressed_button = st.form_submit_button(label="Wyślij")
    if pressed_button:
        input_data = {
            "rok_budowy": rok_budowy,
            "liczba_pokoi": liczba_pokoi,
            "pietro": pietro,
            "metraz": metraz,
            "dzielnica": dzielnica,
            "wyposazenie": wyposazenie
        }
        cena = predict_price(model, feature_names, input_data)
        save_to_blob(input_data, cena)
        st.success(f"Szacowana cena mieszkania: {cena:,.2f} zł")