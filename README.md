# Python Celery Instrumentation

This is a sample app to demonstrate how to instrument Python Celery app with **New Relic** and **OpenTelemetry**. This repository has a docker compose file to set up all these services conveniently.

The code is organized into multiple branches. The main branch has the Celery app without any instrumentation. Other branches then build upon the main branch to add specific instrumentations as below:

| Branch                                                                                         | Instrumentation | Code changes for instrumentation                                                                                |
| ---------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- |
| [main](https://github.com/cubeapm/sample_app_python_celery/tree/main)         | None            | -                                                                                                               |
| [newrelic](https://github.com/cubeapm/sample_app_python_celery/tree/newrelic) | New Relic       | [main...newrelic](https://github.com/cubeapm/sample_app_python_celery/compare/main...newrelic) |
| [otel](https://github.com/cubeapm/sample_app_python_celery/tree/otel)         | OpenTelemetry   | [main...otel](https://github.com/cubeapm/sample_app_python_celery/compare/main...otel)         |

# Setup

Clone this repository and go to the project directory. Then run the following commands

```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
docker compose up --build

# Run the following command in a separate terminal to create a task.
python3 send_task.py
```

# Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
