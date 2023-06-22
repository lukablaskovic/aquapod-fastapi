from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTConfig
from mqtt_config import CONFIG_PARAMS
import json
app = FastAPI()

mqtt_config = MQTTConfig(CONFIG_PARAMS)

MQTT = FastMQTT(
    config=mqtt_config
)

MQTT.init_app(app)


@MQTT.on_connect()
def connect(client, flags, rc, properties):
    print("AquaPod FastMQTT Client - Connected: ",
          client, flags, rc, properties)


@MQTT.on_disconnect()
def disconnect(client, packet, exc=None):
    print("AquaPod FastMQTT Client - Disconnected")


@MQTT.subscribe("/aquapods/+/+")
async def handle_messages(client, topic, payload, qos, properties):
    data = (payload.decode())
    # Now you can process the sensor data


@MQTT.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ", topic, payload.decode(), qos, properties)
    data = json.loads(payload.decode())  # decode JSON payload
    print(data)

# uvicorn main:app --host 0.0.0.0 --port 8001 --reload
