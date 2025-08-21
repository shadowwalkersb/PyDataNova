FROM python:3.11-slim

WORKDIR /app/api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/api/fastapi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
