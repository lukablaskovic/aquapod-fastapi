import json
import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"
broker_port = 1883  # Default port for MQTT protocol is 1883
timeout = 60  # [seconds]


def on_connect(client, userdata, flags, rc):
    latitude = 77.5945627
    longitude = 12.9715987
    message = {
        "latitude": latitude,
        "longitude": longitude
    }
    client.publish("/aquapods/Pula/gps-position", json.dumps(message))


client = mqtt.Client(broker_address, broker_port, timeout)
client.connect("localhost", 1883, 60)


def on_publish(client, userdata, mid):
    print("Message Published...")


# Randomly vary the latitude and longitude
# GPS position
latitude = 77.5945627
longitude = 12.9715987


def vary_coordinates(lat, lon, var=0.0001):
    return lat + random.uniform(-var, var), lon + random.uniform(-var, var)


# Simulate AquaPod movement by publishing new GPS position every 5 seconds
try:
    while True:
        latitude, longitude = vary_coordinates(latitude, longitude)

        message = {
            "latitude": latitude,
            "longitude": longitude,
        }

        client.publish("/aquapods/Pula/gps-position",
                       json.dumps(message), qos=1)
        print("Message published")

        time.sleep(5)
except KeyboardInterrupt:
    client.disconnect()
    print("\nScript stopped")
