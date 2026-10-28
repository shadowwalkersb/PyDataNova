"""Small HTTP bridge for the browser-based Kafka demo."""

import json
import os
import time
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError


BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = "pydatanova.events"

app = FastAPI(title="PyDataNova Kafka Demo")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ready", "topic": TOPIC}


@app.post("/events")
def trigger_event() -> dict[str, object]:
    event = {
        "event_id": str(uuid.uuid4()),
        "type": "demo.button_clicked",
        "message": "The PyDataNova Kafka button was clicked",
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
        request_timeout_ms=10_000,
    )
    try:
        metadata = producer.send(TOPIC, event).get(timeout=10)
    except KafkaError as exc:
        raise HTTPException(status_code=503, detail=f"Could not publish to Kafka: {exc}") from exc
    finally:
        producer.close()

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=f"pydatanova-browser-demo-{uuid.uuid4()}",
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
        consumer_timeout_ms=10_000,
    )
    try:
        for message in consumer:
            if message.value.get("event_id") == event["event_id"]:
                return {
                    "topic": metadata.topic,
                    "partition": metadata.partition,
                    "offset": metadata.offset,
                    "event": message.value,
                }
        raise HTTPException(status_code=504, detail="Kafka received the event but the demo consumer timed out")
    finally:
        consumer.close()
