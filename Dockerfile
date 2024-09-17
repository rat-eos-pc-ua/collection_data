FROM python:3.8

WORKDIR /app

COPY requirements.txt config.json /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "collection.py"]
