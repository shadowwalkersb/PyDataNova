FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r fastapi_service/requirements.txt
CMD ["uvicorn", "fastapi_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
