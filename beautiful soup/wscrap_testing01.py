#req module
#python -m pip install beautifulsoup4
#https://pypi.python.org/pypi/beautifulsoup4

#http request header field
#https://www.tutorialspoint.com/http/http_requests.htm
#https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields

#http request header editor
#http://www.diveintopython.net/http_web_services/user_agent.html

#python -m pip install lxml

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#print(source) #html data [not tree source]
#print(source)
soup = bs.BeautifulSoup(source,'lxml')
print("soup.title : get all title syntax")
print((soup.title))
print("\n")
print("soup.title.name : title word")
print((soup.title.name))
print("\n")
print("soup.title.string : get string in syntax only")
print((soup.title.string))
print("\n")
print("soup.find_all('p') : find all paragraph[p]")
print(str(soup.find_all('p')))
print("\n")
print("soup.find_all('p') : find all paragraph[p] with loop for : line to line")
for paragraph in soup.find_all('p'):
    print(paragraph)
print("\n")
print(".string if double quote not display")
for paragraph in soup.find_all('p'):
    print(str(paragraph.string))
print("\n")
print(".text all text")
for paragraph in soup.find_all('p'):
    print((paragraph.text))
print("\n")
print("soup.get_text()")
print(soup.get_text())
print("\n")
print("get url:get href value in href only")
for url in soup.find_all('a'):
    print(url.get('href'))