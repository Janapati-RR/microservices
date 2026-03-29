FROM python:3.11-slim

# Set environment variables for clarity and consistency
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

WORKDIR $APP_HOME

# Create a non-root user and group to run the application for security
RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --ingroup appgroup appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Switch to the non-root user
USER appuser

# Start the app using Gunicorn for production-readiness
EXPOSE 8080
CMD exec gunicorn --bind :${PORT:-8080} --workers 1 --threads 8 --timeout 120 main:app
