import zipfile, urllib.request, shutil
# ref https://stackoverflow.com/questions/9419162/python-download-returned-zip-file-from-url
#python3 only
url = 'http://www.brushlovers.com/item/download/?id=6458'
file_name = 'myzip.zip'

response =  urllib.request.urlopen(url)
out_file = open(file_name, 'wb')
shutil.copyfileobj(response, out_file)
#zf = zipfile.ZipFile(file_name)
#zf.extractall()
out_file.close