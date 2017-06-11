import urllib.request
import shutil
import zipfile
#work for zipfile like..rar.
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

out_file = open(location_filedestination, 'wb')
shutil.copyfileobj(filesource,out_file,prelog="download : ",disp_log=True)
out_file.close

