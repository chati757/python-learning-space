import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import ssl

topics = "testtopic"

auth = {
  'username':"testuser",
  'password':"testuser"
}

tls = {
  'ca_certs':"./certificate/addtrustexternalcaroot.crt",
  'tls_version':ssl.PROTOCOL_TLSv1_2
}

'''
publish.single(
  topics,
  payload="hello world",
  hostname="m13.cloudmqtt.com",
  client_id="wuolgjlj",
  auth=auth,
  tls=tls,
  port=34081,
  protocol=mqtt.MQTTv311
  )
'''

subscribe.simple(
    topics,
    hostname="m13.cloudmqtt.com",
    qos=0,
    port=34081, 
    client_id="web_eb4e9e6b", 
    transport="websockets",
    keepalive=60, 
    auth=auth, 
    tls=tls,
    protocol=mqtt.MQTTv311
    )