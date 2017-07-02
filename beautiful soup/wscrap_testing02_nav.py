import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://www.brushlovers.com/web/photoshop-brush/diversity-of-species.html').read()
soup = bs.BeautifulSoup(source,'lxml')

#nav tag
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

print("find image")
select = soup.select(".item-image > a > img")
print(select)
print("\n")

print("find image2")
select = soup.select_one(".item-image > a > img")
print(select)
print("\n")
print(select["src"])
print("\n")