# ---- Python 3.11, slim, wheels rapides
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# OS deps (compacts) pour wheels éventuels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dépendances
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip wheel setuptools && \
    pip install -r requirements.txt

# App
COPY . /app

# Streamlit écoute sur $PORT fourni par Render
EXPOSE 10000
CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
