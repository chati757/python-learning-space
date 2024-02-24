import psutil

pid = input("input pid to terminate : ")
psutil.Process(int(pid)).terminate()