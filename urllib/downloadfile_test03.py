import urllib.request
import shutil
#ref https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
# Download the file from `url` and save it locally under `file_name`:
#url download https://static.brusheezy.com/system/protected/files/000/012/681/MARIALACAMBRA_MADERAS_JPG.zip?md5=DZm0csXUEAeqYbIDXGrwqQ&expires=1497027561
url = "http://www.brushlovers.com/item/download/?id=6458"
print("--download form url--")
print(url)
filesource = urllib.request.urlopen(url)

meta = filesource.info()
print("---meta data---")
print(meta)

print("---file_size---")
array_meta=str(meta).split("\n")
for linemeta in array_meta:
    if(linemeta.find("Content-Length")==0):
        print(linemeta)
        
print("--source file--")
print(filesource)

filedestination = "test.rar"
print("--destinationfile name--")
print(filedestination)

block_sz = 8192 # 8192 index form tell function
print("---block size---")
print(block_sz)
#buffer = filesource.read(block_sz)
#print("---buffer read form block size---")
#print(buffer)

file_size_dl = 0 # first files size [download file]
print("initalize files size at zero")
print(file_size_dl)

location_filedestination = "./"+filedestination
print("set location of file destination")
print(location_filedestination)
'''
out_file = open(location_filedestination, 'wb')

while True:
    buffer = filesource.read(block_sz)
    if not buffer:
        break
    file_size_dl += len(buffer)
    out_file.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    f.close()

shutil.copyfileobj(location_filedestination,out_file)
'''

'''
file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

    f.close()
'''