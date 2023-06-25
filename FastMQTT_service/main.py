from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTConfig
from FastMQTT_service.mqtt_config import CONFIG_PARAMS
import json
import asyncio
import aiohttp

app = FastAPI()
REST_API_URL = "http://localhost:8000"

mqtt_config = MQTTConfig(CONFIG_PARAMS)

fast_mqtt = FastMQTT(
    config=mqtt_config
)

fast_mqtt.init_app(app)


@app.on_event("startup")
async def startup_event():
    global session
    session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()


@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    print("AquaPod FastMQTT Client - Connected: ",
          client, flags, rc, properties)


@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("AquaPod FastMQTT Client - Disconnected")


"""
QoS2, Exactly once: The message is always delivered exactly once. 
The message must be stored locally at the sender, until the sender receives confirmation that the message has been published by the receiver.
The message is stored in case the message must be sent again.
QoS2 is the safest, but slowest mode of transfer. 
A more sophisticated handshaking and acknowledgement sequence is used than for QoS1 to ensure no duplication of messages occurs.
https://www.eclipse.org/paho/files/mqttdoc/MQTTClient/html/qos.html
"""


@app.get("/")
async def publish_message(topic, payload):
    fast_mqtt.publish(topic, json.dumps(payload), qos=2)


# On message received from the client, send request to HTTP_REST_service


@fast_mqtt.subscribe("/aquapods/+/+")
async def handle_messages(client, topic, payload, qos, properties):
    data = json.loads(payload.decode())

    url = REST_API_URL + topic
    resp_text = await send_data(url, data)
    print(resp_text)


async def send_data(url: str, data: dict):
    async with session.post(url, json=data) as resp:
        return await resp.text()

# Run with: uvicorn main:app --host 0.0.0.0 --port 8001 --reload
