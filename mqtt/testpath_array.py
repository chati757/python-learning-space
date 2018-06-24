import os
import urllib.parse as urlparse

url_str = 'test'

print("url_str:"+url_str)
print("url_str[1:]"+url_str[1:])

url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://zzjsmgiu:nsAHn104ezdV@m20.cloudmqtt.com:13049')
url = urlparse.urlparse(url_str)

print(url_str)
print(url)
print(url.username)
print(url.passowrd)