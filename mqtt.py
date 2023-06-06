from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTConfig
import json
app = FastAPI()

mqtt_config = MQTTConfig()

mqtt = FastMQTT(config=mqtt_config)

mqtt.init_app(app)


@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("test")  # subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)


"""
@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ", topic, payload.decode(), qos, properties)
"""


@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ", topic, payload.decode(), qos, properties)
    data = json.loads(payload.decode())  # decode JSON payload
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f"Coordinates are {latitude}, {longitude}")
