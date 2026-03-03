FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy all environment files
COPY . /app/

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install pinned dependencies
RUN pip install --no-cache-dir -r requirements.txt