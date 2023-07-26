import threading
import time

def interrupt_sleep():
    print("Interrupting sleep")

# Create a thread that will interrupt the sleep in 5 seconds
thread = threading.Timer(5, interrupt_sleep)
thread.start()

# Sleep for 10 seconds
time.sleep(10)

print("Sleep completed")