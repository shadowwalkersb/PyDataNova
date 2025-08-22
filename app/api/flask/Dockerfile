FROM python:3.11-slim
WORKDIR /app/
COPY . .
RUN pip install --no-cache-dir -r flask/requirements.txt
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "2"]
