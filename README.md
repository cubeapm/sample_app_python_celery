# Python Celery OpenTelemetry Instrumentation

This is a sample app to demonstrate how to instrument Python Celery app with OpenTelemetry. This repository has a docker compose file to set up conveniently.

This repository is inentionally designed to work with any OpenTelemetry backend, not just CubeAPM. In fact, it can even work without any OpenTelemetry backend (by dumping traces to console, which is also the default behaviour).

## Setup

Clone this repository and go to the project directory. Then run the following commands

```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
docker compose up --build

# Run the following command in a separate terminal to create a task.
python3 send_task.py
```

Traces are printed to console (where docker compose is running) by default. If you want to send traces to a backend tool, comment out the `OTEL_LOG_LEVEL` line and uncomment the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` line in [docker-compose.yml](docker-compose.yml).

## Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
