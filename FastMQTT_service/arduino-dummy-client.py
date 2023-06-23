import json
import paho.mqtt.client as mqtt
import time
import random
import logging

# Broker connection settings
broker_address = "localhost"
broker_port = 1883  # Default port for MQTT protocol is 1883
timeout = 60  # [seconds]

# Setup logging
logging.basicConfig(level=logging.INFO)

# Function to vary GPS coordinates


def vary_coordinates(lat, lon, var=0.0001):
    return lat + random.uniform(-var, var), lon + random.uniform(-var, var)

# Callback function for MQTT client connection


def on_connect(client, userdata, flags, rc):
    logging.info("Connected to MQTT broker")

# Callback function for MQTT message publish


def on_publish(client, userdata, mid):
    logging.info(f"Message {mid} delivered\n")

# Main function


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Enable MQTT client logger
    client.enable_logger()

    # Connect to the broker
    try:
        client.connect(broker_address, broker_port, timeout)
    except Exception as e:
        logging.error(f"Could not connect to MQTT broker: {e}")
        return

    # Start the client loop
    client.loop_start()

    # Initial GPS position
    latitude = 77.5945627
    longitude = 12.9715987

    # Simulate AquaPod movement by publishing new GPS position every 5 seconds
    try:
        while True:
            latitude, longitude = vary_coordinates(latitude, longitude)
            message = {
                "latitude": latitude,
                "longitude": longitude,
            }

            msg_info = client.publish(
                "/aquapods/Pula/gps-position", json.dumps(message), qos=1)

            if msg_info.rc != mqtt.MQTT_ERR_SUCCESS:
                logging.error("Failed to publish message")
            else:
                logging.info(f"Message published, message ID: {msg_info.mid}")

            time.sleep(5)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
        logging.info("Script stopped")


if __name__ == "__main__":
    main()
