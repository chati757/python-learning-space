import urllib.request
# works well only for small files.
# Download the file from `url` and save it locally under `file_name`:
response = urllib.request.urlopen("http://www.brushlovers.com/item/download/?id=6458") 
out_file = open("test.rar", 'wb')
data = response.read() # a `bytes` object
out_file.write(data)

