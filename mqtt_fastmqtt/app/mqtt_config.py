CONFIG_PARAMS = dict(
    host="mqtt_broker",  # Define your MQTT broker here
    # LOCAL: host="mqtt.mosquito.org",
    port=1883,
    keepalive=60,  # seconds
    username=None,
    password=None)

REST_API_URL = "http://http_fastapi:80"
# LOCAL: REST_API_URL = "http://localhost:8000"
