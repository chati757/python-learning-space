import urllib.request
# works well only for small files.
# Download the file from `url` and save it locally under `file_name`:
response = urllib.request.urlopen("http://my-brushes.s3.amazonaws.com/images/items/a5f1f101adb382ed52c1db951ad31635e64a5787/Diversity_of_Species___Brushes_by_scumbugg-o.jpg?v=5") 
out_file = open("test.jpg", 'wb')
data = response.read() # a `bytes` object
out_file.write(data)

