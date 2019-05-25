import json
import urllib.request


url = ''
raw_data = urllib.request.urlopen(url)
json_data_buffer = json.loads(raw_data.read().decode())

print(json_data_buffer)