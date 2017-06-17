'''
import urllib.request
#checking : httpbin.org  

req = urllib.request.Request(
    "http://httpbin.org/user-agent",
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
'''


#ref :https://pythonprogramming.net/urllib-tutorial-python-3/
import urllib.request
url = 'http://httpbin.org/user-agent'

# now, with the below headers, we defined ourselves as a simpleton who is
# still using internet explorer.
headers = {}
headers['User-Agent'] = "Mozilla/5.0"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)

'''
import urllib.request
import sys
req = urllib.request.Request(
    "http://httpbin.org/user-agent"
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
f.close()

print("sys.version[:3]")
print(sys.version[:3])
'''