FROM python:3.11-slim
WORKDIR /app/
COPY . .
RUN pip install --no-cache-dir -r flask_service/requirements.txt
CMD ["sh", "-c", "gunicorn flask_service.app:app -b 0.0.0.0:$PORT -w 2"]
