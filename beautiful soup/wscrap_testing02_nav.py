import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

#nav tag
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