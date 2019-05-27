import tempfile
import os
actual_name = "test_temp_file"

with tempfile.NamedTemporaryFile(dir='./tempfile') as temp:
  temp.name = "test_temp_file"
  print(temp.name)
  temp.write(b'working')
  temp.seek(0)
  print(temp.read())
  input("pause:")
  temp.close()