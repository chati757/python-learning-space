#download with GET url
import requests
print("downloading with requests")
url = 'http://www.brushlovers.com/item/download/?id=6458'
r = requests.get(url)
with open("test.rar", "wb") as code:
    code.write(r.content)