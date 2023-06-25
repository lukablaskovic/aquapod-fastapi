# 

<div align="center">
  <h1>Aquapod FastAPI</h1>  
  <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
</div>

*AquaPod* is an innovative project designed to address marine pollution by autonomously collecting waste from the sea. This repository hosts the code for the REST API built using *FastAPI*, used to control the AquaPod, as well as fetch sensor and other relevant data.

This repository comprises two distinct services:

1. `HTTP_REST_service`: This service interfaces with the AquaPod frontend Vue application. It's responsible for relaying HTTP requests and responses between the Vue application and the FastAPI server.

2. `FastMQTT_service`: This service communicates with the Arduino onboard the AquaPod boat. It uses the MQTT protocol, a lightweight messaging protocol often used in IoT systems, to send and receive data to and from the Arduino.

<hr />

<figure>
  <img
  src="aquapod_diagram.png?raw=true"
  alt="Encryption with MQTT.">
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

### Install all the modules first:
```bash
pip install -r requirements.txt
```

## HTTP_REST_service

### To run the service:

```bash
cd HTTP_REST_service
```

```bash
uvicorn main:app --reload
```

```bash
### Environment variables:
Linux, macOS, Windows Bash

export UVICORN_USER="fillme" \
export UVICORN_PASSWORD="fillme" \
export  UVICORN_HOST="fillme" \
export UVICORN_DATABASE="aquapod" \
export JWT_SECRET=fillme
```
By default, HTTP_REST_service runs on port 8000.

<hr />

## FastMQTT_service
The AquaPod, running on Arduino (**Node A**), connects to an MQTT broker and publishes data to it. The FastAPI server (**Node B**), subscribed to the relevant topics on the MQTT broker, receives this data for further processing and use in the application.

### MQTT broker - Mosquitto
The MQTT protocol operates on a client/server model. The broker (server) is essential as it routes messages between clients based on the topics of messages.

In our project, the AquaPod's Arduino publishes sensor data to an MQTT broker. Our FastMQTT_service, subscribed to the broker, receives this data for further processing.

We're using [Mosquitto](https://mosquitto.org/), an open-source MQTT broker. However, other brokers such as HiveMQ, RabbitMQ or cloud solutions like AWS IoT can also be used.

### To run the MQTT service:

```bash
cd FastMQTT_service
```

```python
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

You can simulate the AquaPod's movements using the **arduino-dummy-client.py** script, which is built using the Paho MQTT client. This script publishes a new GPS position every 5 seconds, mimicking real-time data from the AquaPod's movement in the sea.

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

```python
pytest
```
