FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Definir las variables de entorno
ENV MONGO_HOST=mongo
ENV MONGO_PORT=27017

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
