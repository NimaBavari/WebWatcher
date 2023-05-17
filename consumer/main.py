import json

import psycopg2
from constants import KAFKA_URI, POSTGRES_URI, SSL_CAFILE, SSL_CERTFILE, SSL_KEYFILE, TOPIC_NAME
from kafka import KafkaConsumer

conn = psycopg2.connect(POSTGRES_URI)

cur = conn.cursor()
cur.execute(
    """create table if not exists reports(
        id serial not null primary key,
        url varchar(200) not null,
        response_time real not null,
        status_code integer not null,
        pattern_matches text[],
        timestamp timestamp default current_timestamp
    );"""
)

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_URI,
    value_deserializer=lambda val: json.loads(val.decode("utf-8")),
    security_protocol="SSL",
    ssl_cafile=SSL_CAFILE,
    ssl_certfile=SSL_CERTFILE,
    ssl_keyfile=SSL_KEYFILE,
)
for message in consumer:
    cur.execute(
        """insert into reports (url, response_time, status_code, pattern_matches) values (%s, %s, %s, %s);""",
        (message["url"], message["response_time"], message["status_code"], message["pattern_matches"]),
    )
    conn.commit()
