import os

TOPIC_NAME = "network_report"
PERIOD = 3600  # once an hour

# List of websites (for demonstration purposes only)
LIST_WEBSITES = [
    {"url": "https://stackoverflow.com/questions", "regexp_pattern": r"\bS\w+"},
    {"url": "https://en.wikipedia.org/wiki/Sequence", "regexp_pattern": r"\w+\s"},
    {"url": "https://www.linkedin.com"},
]

# Aiven services
KAFKA_URI = "kafka-367b4f0c-take-home-assignment.aivencloud.com:15478"

# SSL file locations
SSL_CAFILE = os.path.abspath("./ca.pem")
SSL_CERTFILE = os.path.abspath("./service.cert")
SSL_KEYFILE = os.path.abspath("./service.key")
