# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

# For Websocket connection
myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
# For Websocket
myMQTTClient.configureEndpoint("a1zetnmz2w4vck.iot.us-east-2.amazonaws.com", 443)
# For TLS mutual authentication with TLS ALPN extension
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)

# For Websocket, we only need to configure the root CA
myMQTTClient.configureCredentials("./certificate/aws-iot-rootCA.crt")
# AWS IoT MQTT Client
# myMQTTClient.configureIAMCredentials(obtainedAccessKeyID, obtainedSecretAccessKey, obtainedSessionToken)
# https://console.aws.amazon.com/iam/ --> users --> create access key
myMQTTClient.configureIAMCredentials("AKIAIMPUZ4N6PLLCB2VA","sXWou67p1ZJSKMua3kaOZ7r2BThOonLTkKNA5xQu", "")

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(client)
    print(userdata)
    print("from topic: ")
    print(message.topic)
    print(message.payload)
    print("--------------\n\n")
    
# Suback callback
def customSubackCallback(mid, data):
    print("Received SUBACK packet id: ")
    print(mid)
    print("Granted QoS: ")
    print(data)
    print(data.message)
    print("++++++++++++++\n\n")

myMQTTClient.connect()
#myMQTTClient.publish("mint-planet-device", "myPayload", 0)
myMQTTClient.subscribe("mint-planet-device", 1, customCallback)
time.sleep(20)
#myMQTTClient.unsubscribe("mint-planet-device")
#myMQTTClient.disconnect()