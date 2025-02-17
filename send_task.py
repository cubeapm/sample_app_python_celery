from redis import Redis
import json
import base64
import uuid


redis_conn = Redis(host='localhost', port=6379, decode_responses=True)


def send_message(base64_encoded_body):
    id = str(uuid.uuid4())
    message = {
        "body": base64_encoded_body,
        "properties": {
            "correlation_id": id,
            "delivery_mode": 2,
            "delivery_info": {
                "exchange": "",
                "routing_key": "celery",
            },
            "priority": 0,
            "body_encoding": "base64",
            "delivery_tag": str(uuid.uuid4()),
        },
        "headers": {
            "id": id,
            "root_id": id,
            "lang": "py",
            "task": "my-task",
            "retries": 0,
            "origin": "gen78948@Dublin",
            "ignore_result": False,
        },
        "content-encoding": "utf-8",
        "content-type": "application/json",
    }

    redis_conn.lpush('celery', json.dumps(message))


if __name__ == "__main__":
    message_body = json.dumps(
        [
            [
                {
                    "my_key": "my_value",
                }
            ],
            {},
            {"chain": None, "chord": None, "callbacks": None, "errbacks": None},
        ]
    )
    base64_encoded_body = base64.b64encode(message_body.encode("utf-8")).decode("utf-8")
    send_message(base64_encoded_body)
