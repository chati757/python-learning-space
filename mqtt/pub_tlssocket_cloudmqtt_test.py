
#python3 -m pip install paho-mqtt
import paho.mqtt.client as mqtt
import os
import urllib.parse as urlparse
import ssl

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("on_connect:rc: " + str(rc))

def on_message(client, obj, msg):
    print("on_message" + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("on_publish:massageid[mid]: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print("on_log:"+string)

#mqttc = mqtt.Client(client_id="web_55",transport="websockets")
mqttc = mqtt.Client(client_id="wuolgjlj",transport="websockets")
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
#mqtt://USER:PASSWORD@host:port
topic = "testtopic"

# tls
'''
tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS, ciphers=None)

'''
mqttc.tls_set(
    cert_reqs=ssl.CERT_REQUIRED,
    certfile="./certificate/client1-key.pem",
    ca_certs="./certificate/addtrustexternalcaroot.crt",
    tls_version=ssl.PROTOCOL_TLSv1_2
    )
# disables peer verification
mqttc.tls_insecure_set(True)
'''
mqttc.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
mqttc.tls_insecure_set(True)
'''
'''
mqttc.tls_insecure_set(True)
If value is set to True, 
it is impossible to guarantee that the host you are connecting to is not impersonating your server. 
This can be useful in initial server testing, 
but makes it possible for a malicious third party to impersonate your server through DNS spoofing
'''
extra_headers={}

# Connect
mqttc.username_pw_set("wuolgjlj","7NEws8XoqYnL")
mqttc.connect(host="m13.cloudmqtt.com",port=34081)

# Start subscribe, with QoS level 0
print("subscribe state")
#mqttc.subscribe(topic, 0)
# Publish a message
print("subscribe state")
mqttc.publish(topic, "my message")

# Continue the network loop, exit when an error occurs
print("loopstate")
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("mainloop rc: " + str(rc))