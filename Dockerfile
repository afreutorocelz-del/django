FROM python:3.11-slim

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /mysite

# Copy requirements first for better caching
COPY requirements.txt /mysite/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /mysite/

# Create a non-root user to run the application
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /mysite
USER appuser

EXPOSE 8000

# Default command (can be overridden in convox.yml)
CMD ["gunicorn", "mysite.wsgi", "--bind=0.0.0.0:8000"]