FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]