FROM python:3.9-slim
EXPOSE 8501

RUN pip install --upgrade pip

WORKDIR /app

COPY streamlit/requirements.txt .

RUN pip install --no-cache-dir -r  requirements.txt

COPY streamlit/test.py .

CMD streamlit run test.py --server.port=8501 --browser.serverAddress="0.0.0.0"