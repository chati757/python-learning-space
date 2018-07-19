
#python3 -m pip install paho-mqtt
import paho.mqtt.client as mqtt
import os
from urllib.parse import urlparse
import ssl
import time
import uuid
import base64

# Define event callbacks
def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))

def on_connect(client, userdata, flags, rc):
    print("on_connect:rc: " + str(rc))

def on_disconnect(client,userdata,rc):
    print("on_disconnect",error_str(rc))

def on_message(client, obj, msg):
    print("on_message" + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("on_publish:massageid[mid]: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print("on_log:"+string)

#mqttc = mqtt.Client(client_id="web_55",transport="websockets")
mqttc = mqtt.Client(protocol=mqtt.MQTTv311,client_id="web_eb4e9e6b",transport="websockets")
sec_websocket_key = uuid.uuid4().bytes
sec_websocket_key = base64.b64encode(sec_websocket_key)
headers = {
        "Host":"m13.cloudmqtt.com:34081",
        "Origin":"https://api.cloudmqtt.com",
        "Upgrade":"websocket",
        "Connection":"Upgrade",
        "Sec-WebSocket-Key":sec_websocket_key.decode("utf8"),
        "Sec-Websocket-Version":"13",
        "Sec-Websocket-Protocol":"mqtt",
        "Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}
mqttc.ws_set_options(path="/mqtt",headers=headers)
#mqttc = mqtt.Client(client_id="web_55",transport="websockets")

# Parse CLOUDMQTT_URL (or fallback to localhost)
#mqtt://USER:PASSWORD@host:port

# Assign event callbacks
print("set event callback")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
mqttc.on_log = on_log
mqttc.enable_logger()

# tls
'''
tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS, ciphers=None)

'''
#Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)

print("set tls_set")
mqttc.tls_set(
    keyfile="./certificate/client1-key.pem",
    certfile="./certificate/client1-crt.pem",
    ca_certs="./certificate/addtrustexternalcaroot.crt",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1_2
    )
# disables peer verification
#mqttc.tls_insecure_set(False)

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

# Connect
print("set username")
mqttc.username_pw_set("testuser","testuser")
mqttc.will_set(topic='testtopic',payload='Connection Closed abnormally..!',qos=0,retain=False)
print("connecting..")
mqttc.connect(host="m13.cloudmqtt.com",port=34081,keepalive=30)
print("connected..")

topic = "testtopic"
'''
# Start subscribe, with QoS level 0
print("subscribe state")
mqttc.subscribe(topic,0)
# Publish a message
#print("publish state")
#mqttc.publish(topic, "my message")

# Continue the network loop, exit when an error occurs
print("loopstate")
#mqttc.loop_forever()
rc = 0
while rc == 0:
    rc = mqttc.loop()
print(error_str(rc))
'''