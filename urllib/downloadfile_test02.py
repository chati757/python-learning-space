import urllib2
# use python2 only
# cannot download rar file
url = "http://www.brushlovers.com/item/download/?id=6458"

#file_name = url.split('/')[-1] #?id=6458
file_name = "testfilename.rar"
print("---file_name---")
print(file_name)
u = urllib2.urlopen(url)
print(u) #<addinfourl at 44287640 whose fp = <socket._fileobject object at 0x02AD2B30>>
f = open(file_name,'wb') #wb write binary
meta = u.info()
print("---meta data---")
print(meta)
print("---file_size---")
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)
file_size_dl = 0
print("---determine file_size_download---")
print(file_size_dl)
block_sz = 8192 # 8192 index form tell function
print("---block size---")
print(block_sz)
buffer = u.read(block_sz)
print("---buffer read form block size---")
print(buffer)
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
