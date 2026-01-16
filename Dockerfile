# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for pandas/scikit-learn if needed
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (Fly.io will map this)
EXPOSE 8080

# Set environment variable for Fly.io
ENV PORT=8080

# Run the application using uvicorn
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}

