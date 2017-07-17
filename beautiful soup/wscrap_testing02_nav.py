import bs4 as bs
import urllib.request
import re

req = urllib.request.Request(
    "https://www.thingiverse.com/thing:1795648",
    data=None,
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
)

source = urllib.request.urlopen(req).read()
soup = bs.BeautifulSoup(source,'lxml')

#nav tag
'''
print(soup.encode('utf-8'))
print("find href in nav link")
print("\n")
nav = soup.nav
for link in nav.find_all('a'):
    print(link.get('href').encode('utf-8'))
print("\n")

print("find text in body class at paragraph tag Ex.<div class='body'><div='brabra'><p>..</div></div>")
print("\n")
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text.encode('utf-8'))
print("\n")


print("find text in div tag class body Ex.<div class='body'></div>")
print("\n")
for div in soup.find_all('div',class_='body'):
    print(div.text.encode('utf-8'))
print("\n")
'''
print("find image")
select = soup.select(".thing-header-data > h1")
print(select[0].get_text())
print("\n")

print("find image2")
select = soup.select_one(".item-image > a > img")
print(select)
print("\n")
print(select["src"])
print("\n")

#head > <mata name="description" content="[target]">
print("find description")
head = soup.head
for count,link in enumerate(head.find_all('meta',attrs={"name":"description"})):
    print(count+1)
    print(link.get('content'))
print("\n")

print("find description2")
div = soup.body
for link in (div.find_all('div',class_="show-more")):
    print(link.text)
print("\n")

print("download resource")
for div in soup.find_all("a"):
    test_search=re.search("./download/.",str(div.get("href")))
    if(test_search):
        print(div.get("href"))
    
print("\n")