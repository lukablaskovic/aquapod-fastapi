from fastapi_mqtt import MQTTConfig

mqtt_config = MQTTConfig(
    host="mqtt_broker",  # Define your MQTT broker here,  # LOCAL: host="localhost", # DOCKER: host="mqtt_broker"
    port=1883,
    keepalive=60,  # seconds
    username=None,
    password=None,
)

REST_API_URL = "http://http_fastapi:80"  # LOCAL: "http://localhost:8000" # DOCKER: "http://http_fastapi:80"
