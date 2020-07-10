import socket
import ssl
import adafruit_minimqtt.adafruit_minimqtt as MQTT

MQTT.socket_module = socket
MQTT.ssl_context = ssl.create_default_context()

### Topic Setup ###

# MQTT Topic
# Use this topic if you'd like to connect to a standard MQTT broker
mqtt_topic = "test/topic"

# Adafruit IO-style Topic
# Use this topic if you'd like to connect to io.adafruit.com
# mqtt_topic = 'aio_user/feeds/temperature'

### Code ###

# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connect(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to MQTT Broker!")
    print("Flags: {0}\n RC: {1}".format(flags, rc))


def disconnect(client, userdata, rc):
    # This method is called when the client disconnects
    # from the broker.
    print("Disconnected from MQTT Broker!")


def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


def unsubscribe(client, userdata, topic, pid):
    # This method is called when the client unsubscribes from a feed.
    print("Unsubscribed from {0} with PID {1}".format(topic, pid))


def publish(client, userdata, topic, pid):
    # This method is called when the client publishes data to a feed.
    print("Published to {0} with PID {1}".format(topic, pid))


# Set up a MiniMQTT Client
client = MQTT.MQTT(
    broker="BROKER_ADDRESS", username="YOUR_USERNAME", password="YOUR_PASSWORD"
)

# Connect callback handlers to client
client.on_connect = connect
client.on_disconnect = disconnect
client.on_subscribe = subscribe
client.on_unsubscribe = unsubscribe
client.on_publish = publish

print("Attempting to connect to %s" % client.broker)
client.connect()

print("Subscribing to %s" % mqtt_topic)
client.subscribe(mqtt_topic)

print("Publishing to %s" % mqtt_topic)
client.publish(mqtt_topic, "Hello Broker!")

print("Unsubscribing from %s" % mqtt_topic)
client.unsubscribe(mqtt_topic)

print("Disconnecting from %s" % client.broker)
client.disconnect()
