#!/usr/bin/python
try:
   fh = open("testfile", "w")
   try:
      raise IOError
   finally:
      print("Going to close the file")
      fh.close()

except IOError:
   print("Error: can\'t find file or read data")

#not goto exception below
except Exception as e:
   print('inexcept')
   print(e)