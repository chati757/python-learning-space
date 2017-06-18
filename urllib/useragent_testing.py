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
        'User-Agent': 'Mozilla/5.0 test123'
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


