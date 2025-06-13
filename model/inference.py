import joblib
import pandas as pd
import os

# Wczytaj model i listę cech
model = joblib.load(os.path.join(os.path.dirname(__file__), "model.joblib"))
feature_names = joblib.load(os.path.join(os.path.dirname(__file__), "feature_names.joblib"))

# Hugging Face automatycznie wywoła tę funkcję przy zapytaniu POST
def predict(input):
    """
    Oczekiwany input:
    {
        "rok_budowy": 2000,
        "liczba_pokoi": 3,
        "pietro": 4,
        "metraz": 60,
        "dzielnica": "Wola",
        "wyposazenie": "Tak"
    }
    """
    df = pd.DataFrame([input])
    df_encoded = pd.get_dummies(df)

    for col in feature_names:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[feature_names]
    prediction = model.predict(df_encoded)[0]
    return {"cena": round(prediction, 2)}