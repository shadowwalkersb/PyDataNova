# Clickable Kafka demo

This page lets you trigger an event with a button and watch it go through a
Kafka producer, the `pydatanova.events` topic, and a consumer. The browser page
is served by PyDataNova's existing web service; a small FastAPI bridge publishes
and reads the event through Kafka.

## What the demo names explicitly

| Kafka concept | Demo value |
| --- | --- |
| Topic | `pydatanova.events` |
| Message key | The event's `event_id` (used to route related events consistently) |
| Broker inside Compose | `kafka:9092` |
| Broker from the Mac | `localhost:9094` |
| Browser API | `http://localhost:8002` |
| Consumer group | A fresh `pydatanova-browser-demo-*` group for each event |

The browser first asks the demo API to produce a JSON event and then uses a
Kafka consumer with `earliest` offset lookup to read it back. The result labels
the topic, key, partition, and offset so these Kafka concepts are visible.

## Run with Docker Compose

From the `app/` directory, start just the web page, Kafka, and demo API:

```sh
docker compose -f docker-compose.yml -f kafka_demo/docker-compose.yml up -d --build web kafka kafka-demo-api
```

Open <http://localhost:5500/kafka_demo/> and click **Trigger event**. The page
shows the topic, message key, partition, offset, consumer group, and event JSON.
You can also inspect the demo API and topic list:

```sh
curl http://localhost:8002/health
curl http://localhost:8002/openapi.json
docker compose -f docker-compose.yml -f kafka_demo/docker-compose.yml exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

To stop these demo services without stopping other Compose services:

```sh
docker compose -f docker-compose.yml -f kafka_demo/docker-compose.yml stop web kafka kafka-demo-api
```

## Run with Tilt

From `app/`, run `tilt up`, then open <http://localhost:5500/kafka_demo/>.
Tilt starts Kafka and the demo API along with the rest of the app.

## Optional: run the command-line example

The same broker also supports the original Python round-trip script. From this
directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python round_trip.py
```

The broker exposes `localhost:9094` to tools on your Mac and `kafka:9092` to
services inside Docker. Override the CLI address with
`KAFKA_BOOTSTRAP_SERVERS` if needed. The broker uses ephemeral storage, so topic
data is discarded when its container is removed. This example is for local
learning, not production.
