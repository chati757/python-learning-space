# use for python3 only
import urllib.request
#checking : httpbin.org  
proxy = urllib.request.ProxyHandler({'http':'http://127.0.0.1:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

req = urllib.request.Request(
    "http://httpbin.org/user-agent",
    data=None,
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

'''
# use for python2 only
import urllib2
url = "http://httpbin.org/user-agent"
headers = {} #create object
headers['User-Agent'] = "1234"

proxy = urllib2.ProxyHandler({'http':'http://127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

req = urllib2.Request(url,headers=headers)
print urllib2.urlopen(req).read()
'''


