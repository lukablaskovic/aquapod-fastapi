CONFIG_PARAMS = dict(
    host="mqtt.mosquito.org",  # Define your MQTT broker here
    # LOCAL: host="mqtt.mosquito.org",
    port=1883,
    keepalive=60,  # seconds
    username=None,
    password=None)

print(CONFIG_PARAMS)

REST_API_URL = "http://http_fastapi:80"
# LOCAL: REST_API_URL = "http://localhost:8000"
