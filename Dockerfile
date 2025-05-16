# Użyj obrazu Pythona
FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki
COPY requirements.txt ./
COPY app.py ./

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otwórz port (domyślny Streamlit to 8501)
EXPOSE 8501

# Uruchom aplikację Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
