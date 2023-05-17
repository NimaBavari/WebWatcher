import os

TOPIC_NAME = "network_report"

# Aiven services
POSTGRES_URI = "postgres://avnadmin:AVNS_BBbUGlvhnVnfyAKCv2H@pg-8301b4f-take-home-assignment.aivencloud.com:15476/defaultdb?sslmode=require"
KAFKA_URI = "kafka-367b4f0c-take-home-assignment.aivencloud.com:15478"

# SSL file locations
SSL_CAFILE = os.path.abspath("./ca.pem")
SSL_CERTFILE = os.path.abspath("./service.cert")
SSL_KEYFILE = os.path.abspath("./service.key")
