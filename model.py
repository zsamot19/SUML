import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
import os

np.random.seed(42)

dzielnice = [
    "Bemowo", "Białołęka", "Bielany", "Mokotów", "Ochota", "Praga-Południe",
    "Praga-Północ", "Rembertów", "Śródmieście", "Targówek", "Ursus", "Ursynów",
    "Wawer", "Wesoła", "Wilanów", "Włochy", "Wola", "Żoliborz"
]

def generate_data(n_samples=1000):
    data = {
        "rok_budowy": np.random.randint(1950, 2023, size=n_samples),
        "liczba_pokoi": np.random.randint(1, 6, size=n_samples),
        "pietro": np.random.randint(0, 15, size=n_samples),
        "metraz": np.random.uniform(20, 150, size=n_samples),
        "dzielnica": np.random.choice(dzielnice, size=n_samples),
        "wyposazenie": np.random.choice(["Tak", "Nie"], size=n_samples)
    }
    df = pd.DataFrame(data)
    
   
    base_price = df['metraz'] * 12000  
    correction = (2023 - df['rok_budowy']) * -50 
    room_bonus = df['liczba_pokoi'] * 20000
    floor_bonus = df['pietro'] * 1000
    equipment_bonus = np.where(df['wyposazenie'] == "Tak", 25000, 0)
    district_bonus = np.random.normal(0, 30000, size=n_samples)  
    df['cena'] = base_price + correction + room_bonus + floor_bonus + equipment_bonus + district_bonus
    return df

df = generate_data()


df_encoded = pd.get_dummies(df, columns=["dzielnica", "wyposazenie"], drop_first=True)
X = df_encoded.drop(columns=["cena"])
y = df_encoded["cena"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred):,.2f} zł")

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.joblib")
joblib.dump(X.columns.tolist(), "model/feature_names.joblib")


with open("model/README.md", "w") as f:
    f.write(
        "# Model predykcji cen mieszkań\n"
        "Model regresyjny RandomForest trenujący na sztucznych danych.\n"
    )

