import json
import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    longitude = 77.5945627
    latitude = 12.9715987
    message = {
        "longitude": latitude,
        "latitude": longitude
    }
    client.publish("/aquapods/Pula/GPSPosition", json.dumps(message))


def on_publish(client, userdata, mid):
    print("Message Published...")


# mqtt.Client.connected_flag = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.connect("localhost", 1883, 60)

client.loop_start()
print("in Main Loop")
client.loop_stop()

client.disconnect()