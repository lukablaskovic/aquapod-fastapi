# aquapod-fastapi

*AquaPod* is an innovative project designed to address marine pollution by autonomously collecting waste from the sea. This repository hosts the code for the REST API built using *FastAPI*, used to control the AquaPod, as well as fetch sensor and other relevant data.

### Install all the modules first:
```
pip install -r requirements.txt
```

### To run the API:
```
uvicorn main:app --reload
```
### Environment variables:
Linux, macOS, Windows Bash
```
export UVICORN_USER="fill_me"
export UVICORN_PASSWORD="fill_me"
export UVICORN_HOST="fill_me"
export UVICORN_DATABASE="aquapod"
export JWT_SECRET="secret"

```
### For Windows Powershell, do:
```
$Env:UVICORN_USER = "fill_me"
...
```
## MQTT
The AquaPod, running on Arduino (**Node 1**), connects to an MQTT broker and sends sensor data to it. The FastAPI server (**Node 2**), subscribed to the relevant topics on the MQTT broker, receives this data for further processing and use in the application.
<figure>
  <img
  src="https://docs.arduino.cc/static/9eebc9b3f4e70e29dbcbfed169496262/4ef49/UnoWiFiRev2_T2_IMG01.png"
  alt="Encryption with MQTT.">
  <figcaption>Encryption with MQTT - docs.arduino.cc</figcaption>
</figure>

### MQTT broker - Mosquitto
The Mosquitto broker is a MQTT server running on your local machine, enabling communication between different clients using the MQTT protocol for sending and receiving messages.
https://mosquitto.org/
```
mqtt % mosquitto_pub -h localhost -t test -m "Hello, World"
```
