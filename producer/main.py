import json
import re
import time

import requests
from constants import KAFKA_URI, LIST_WEBSITES, PERIOD, SSL_CAFILE, SSL_CERTFILE, SSL_KEYFILE, TOPIC_NAME
from kafka import KafkaProducer


def check_website(url: str, regexp_pattern: str | None = None) -> dict | None:
    try:
        resp = requests.get(url, timeout=3)
    except requests.ConnectTimeout:
        return None
    matches = []
    if regexp_pattern is not None:
        matches = re.findall(regexp_pattern, resp.text)
    return {
        "URL": url,
        "response_time": resp.elapsed.total_seconds(),
        "status_code": resp.status_code,
        "pattern_matches": matches,
    }


producer = KafkaProducer(
    bootstrap_servers=KAFKA_URI,
    value_serializer=lambda val: json.dumps(val).encode("utf-8"),
    security_protocol="SSL",
    ssl_cafile=SSL_CAFILE,
    ssl_certfile=SSL_CERTFILE,
    ssl_keyfile=SSL_KEYFILE,
)

current_time = time.time()
while True:
    if time.time() - current_time >= PERIOD:
        current_time = time.time()
        for w in LIST_WEBSITES:
            url = w["url"]
            pattern = w["regexp_pattern"] if "regexp_pattern" in w else None
            result = check_website(url, pattern)
            if result is not None:
                producer.send(TOPIC_NAME, result)
        producer.flush()
