from urllib.parse import urlparse

ws_url="wss://m13.cloudmqtt.com:34081/mqtt"

urlparts = urlparse(ws_url)
print(urlparts)
print("host")
print("{0:s}".format(urlparts.netloc))