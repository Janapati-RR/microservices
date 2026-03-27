FROM python:3.11-slim
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Start the app using Gunicorn for production-readiness
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
