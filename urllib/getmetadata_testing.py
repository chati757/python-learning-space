import urllib.request
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

print(filesource.url)
