#

<div align="center">
  <h1>Aquapod FastAPI</h1>  
  <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
</div>

_AquaPod_ 🛥️ is an innovative project designed to address marine pollution by autonomously collecting waste from the sea. This repository hosts the code for the REST API built using _FastAPI_, used to control the AquaPod, as well as fetch sensor and other relevant data.

This repository comprises three distinct services:

1. `http_fastapi`: This service interfaces with the AquaPod frontend Vue application. It's responsible for relaying HTTP requests and responses between the Vue application and the FastAPI server.

2. `mqtt_fastmqtt`: This service communicates with the Arduino onboard the AquaPod boat. It uses the MQTT protocol, a lightweight messaging protocol often used in IoT systems, to send and receive data to and from the Arduino.

3. `arduino-dummy-client`: This service mimics the functionality of the Arduino onboard the AquaPod boat using the Python-based paho.mqtt package. It's designed to simulate the Arduino's behavior for testing and development purposes without needing actual hardware.

<hr />

<figure>
  <img
  src="aquapod_diagram.png?raw=true"
  alt="AquaPod diagram">
</figure>
<hr />

The **AquaPod** system is comprised of several elements as depicted in the diagram above. These elements can be categorized based on their location and function:

**Included in this repository:**

- `HTTP REST API Service`: Handles the server-side operations of the system.
- `PostgreSQL database`: Stores all the essential data.
- `Pytest Service`: Used for testing the components of the system.
- `IoT Edge FastMQTT Service`: Manages MQTT messaging for IoT devices.

**External to this repository:**

- `VUE.js Frontend Application`: Handles the client-side operations of the system.
- `AquaPod Arduino`: The hardware component that interacts with the system.

**Others:**

- `Cloud CDN`: Assists in the delivery of video content across the system.
- `MQTT IoT Core Broker`: Manages MQTT messaging for IoT devices.

<hr />

# How to run?

## 1. Using Docker compose

```bash
cd http_fastapi
```

### Edit env.docker.template

- after editing, rename to .env

### Edit MQTT config

```bash
cd mqtt_fastmqtt
```

```python
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
mqtt_config = MQTTConfig(
    host="mqtt_broker",
    port=1883, # Default
    keepalive=60,  # seconds
    username=None,
    password=None,
)

REST_API_URL = "http://http_fastapi:80"
```

### Arduino client

```python
# Edit Broker connection settings
broker_address = "mqtt_broker"
broker_port = 1883  # Default port for MQTT protocol is 1883
timeout = 60  # [seconds]
```

### Docker compose

Finally, run the following command in root dir:

```bash
docker-compose up -d
```

<figure>
  <img
  src="aquapod_compose.png?raw=true"
  alt="Aquapod docker compose">
</figure>


Finally, explore the interactive REST-API documentation at:   
```bash
http://localhost:8000/docs
```

<hr />

## 2. Manually
Make sure to set up python 3.9 virtual environment first.

### Install all the modules first:

```bash
pip install -r requirements.txt
```

## HTTP_REST_service

### To run the service:

```bash
cd http_fastapi
```

```bash
uvicorn main:app --reload
```

### Edit env.local.template

- after editing, rename to .env

By default, HTTP_REST_service runs on port 8000.

Explore the interactive REST-API documentation at:   
```bash
http://localhost:8000/docs
```

<hr />

## FastMQTT_service

The AquaPod, running on Arduino (**Node A**), connects to an MQTT broker and publishes data to it. The FastAPI server (**Node B**), subscribed to the relevant topics on the MQTT broker, receives this data for further processing and use in the application.

### MQTT broker - Mosquitto

The MQTT protocol operates on a client/server model. The broker (server) is essential as it routes messages between clients based on the topics of messages.

In our project, the AquaPod's Arduino publishes sensor data to an MQTT broker. Our FastMQTT_service, subscribed to the broker, receives this data for further processing.

We're using [Mosquitto](https://mosquitto.org/), an open-source MQTT broker. However, other brokers such as HiveMQ, RabbitMQ or cloud solutions like AWS IoT can also be used.

### To run the MQTT service:

```bash
cd mqtt_fastmqtt
```

### Edit mqtt_config.py

```python
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
mqtt_config = MQTTConfig(
    host="localhost",
    port=1883, # Default
    keepalive=60,  # seconds
    username=None,
    password=None,
)

REST_API_URL = "http://localhost:8000"
```

<hr />

## Arduino dummy client

You can simulate the AquaPod's movement or pump control using the **arduino-dummy-client.py** script, which is built using the Paho MQTT client.

```bash
cd arduino_client
```

### Arduino config

```python
# Edit Broker connection settings
broker_address = "localhost"
broker_port = 1883  # Default port for MQTT protocol is 1883
timeout = 60  # [seconds]
```

### Select main function in arduino-dummy-client.py

```python
if __name__ == "__main__":
    main_test_pump_control()
    # main_test_movement()
```

### Run with:

```python
python3 arduino-dummy-client.py
```

And stop using KeyboardInterrupt.

<hr />

## Pytest Unit Testing

You can validate the functionality and correctness of the AquaPod's REST API using **pytest**. Running these unit tests ensures that all API endpoints respond as expected and helps to identify any potential issues in the API's behavior.

### To run the tests:

```bash
cd Test
```

#### Make sure to include the same .env before running the tests

```python
pytest
```
