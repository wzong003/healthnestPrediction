FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies first (avoids cache issues)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . /app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
