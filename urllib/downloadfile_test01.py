#example url
#http://www.brushlovers.com/item/download/?id=6458

'''
ref from youtube
crawler
https://www.youtube.com/watch?v=XjNm9bazxn8
urllib
https://www.youtube.com/watch?v=Su4nRkiW2NQ&list=PLYj9OBozaypbr9jRLGWmCAODbX1Vr5bb6
Web scraping (beautiful soup)
https://www.youtube.com/watch?v=Su4nRkiW2NQ&list=PLYj9OBozaypbr9jRLGWmCAODbX1Vr5bb6

ref form stack overflow

Example 1
import urllib
urllib.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
---------------------------------------------------------------------------------
Example 2 [have progressbar]
import urllib2

url = "http://www.brushlovers.com/item/download/?id=6458"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name,'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

'''
import urllib.request

def download() : 
    urllib.request.urlretrieve("http://www.brushlovers.com/item/download/?id=6458","testdownload.rar")


if __name__=="__main__":
        download()