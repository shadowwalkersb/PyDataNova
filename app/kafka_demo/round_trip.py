"""Send one JSON event to Kafka and read it back."""

import json
import os
import time
import uuid

from kafka import KafkaConsumer, KafkaProducer


BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9094")
TOPIC = "pydatanova.events"


def main() -> None:
    event = {
        "event_id": str(uuid.uuid4()),
        "type": "demo.greeting",
        "message": "Hello from PyDataNova",
    }

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        key_serializer=lambda key: key.encode("utf-8"),
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )
    try:
        event_key = event["event_id"]
        metadata = producer.send(TOPIC, key=event_key, value=event).get(timeout=10)
        print(f"Produced to topic={metadata.topic} key={event_key} partition={metadata.partition} offset={metadata.offset}: {event}")
    finally:
        producer.close()

    # Use a fresh group so this demo can be rerun and still read its own event.
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=f"pydatanova-demo-{uuid.uuid4()}",
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
        consumer_timeout_ms=10_000,
    )
    try:
        deadline = time.monotonic() + 10
        for message in consumer:
            if message.value.get("event_id") == event["event_id"]:
                message_key = message.key.decode("utf-8") if message.key else None
                print(f"Consumed from topic={message.topic} key={message_key} partition={message.partition} offset={message.offset}: {message.value}")
                return
            if time.monotonic() >= deadline:
                break
        raise TimeoutError("Kafka did not return the event within 10 seconds")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
