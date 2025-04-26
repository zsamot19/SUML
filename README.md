# Aplikacja do szacowania ceny mieszkania

Aplikacja Streamlit, która umożliwia użytkownikowi oszacowanie ceny mieszkania na podstawie wprowadzonych parametrów. Model AI działa **lokalnie** i nie wymaga połączenia z internetem.
Model to klasyfikator regresyjny RandomForestRegressor, wytrenowany na syntetycznych danych opisujących mieszkania w Warszawie. Dane, na których trenowany był model są sytentyczne przez co nie mają odzwierciedlenia w rzeczywistości.

## Technologie
- [Streamlit](https://streamlit.io/)

## Wymagania wstępne
- Python 3.7+
- pip (system zarządzania pakietami Pythona)

## Instalacja
pip install -r requirements.txt

## Uruchomienie aplikacji
streamlit run app.py

## Uwagi
Aktualna wersja wyświetla jedynie komunikat "Wkrótce dostępne" po przesłaniu formularza.
Docelowo aplikacja będzie wykorzystywać model machine learningowy do predykcji cen.
