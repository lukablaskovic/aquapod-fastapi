from fastapi import FastAPI
from fastapi_mqtt import FastMQTT
from .mqtt_config import mqtt_config, REST_API_URL
import json
import aiohttp

app = FastAPI()

fast_mqtt = FastMQTT(config=mqtt_config)

fast_mqtt.init_app(app)


@app.on_event("startup")
async def startup_event():
    try:
        # Attempt to connect to the MQTT broker
        global session
        session = aiohttp.ClientSession()
    except Exception as e:
        print("Failed to connect to MQTT broker:", e)


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()


@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    print("AquaPod FastMQTT Client - Connected: ", client, flags, rc, properties)


@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("AquaPod FastMQTT Client - Disconnected")


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


# Run with: uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
