from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTConfig
from mqtt_config import CONFIG_PARAMS
import json
import asyncio
import aiohttp

app = FastAPI()
REST_API_URL = "http://localhost:8000"

mqtt_config = MQTTConfig(CONFIG_PARAMS)

MQTT = FastMQTT(
    config=mqtt_config
)

MQTT.init_app(app)


@app.on_event("startup")
async def startup_event():
    global session
    session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()


@MQTT.on_connect()
def connect(client, flags, rc, properties):
    print("AquaPod FastMQTT Client - Connected: ",
          client, flags, rc, properties)


@MQTT.on_disconnect()
def disconnect(client, packet, exc=None):
    print("AquaPod FastMQTT Client - Disconnected")

# On message received from the client, send request to HTTP_REST_service


@MQTT.subscribe("/aquapods/+/+")
async def handle_messages(client, topic, payload, qos, properties):
    data = json.loads(payload.decode())

    url = REST_API_URL + topic
    print(data)
    resp_text = await send_data(url, data)
    print(resp_text)


async def send_data(url: str, data: dict):
    async with session.post(url, json=data) as resp:
        return await resp.text()

# Run with: uvicorn main:app --host 0.0.0.0 --port 8001 --reload
