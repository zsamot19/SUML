FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
COPY model.py ./
COPY model/ model/.

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
