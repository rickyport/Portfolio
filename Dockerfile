# Use stable Python version (IMPORTANT)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for pandas/numpy builds if ever required)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip first (prevents many build issues)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run Flask app (production-safe alternative)
CMD ["python", "app.py"]