import os
#print(os.path.isfile(fname)) # return False or True (for check file is exist)
print(os.path.isdir("./home/el")) # return False or True
print(os.listdir(".")) # list file in current directory
os.makedirs("./test") # create folder name is "test"