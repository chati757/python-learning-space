from playsound import playsound
import time

playsound('./tws_search.wav',block=False)
'''
incase error (for downgrade version)
please try : python3 -m pip install playsound==1.2.2
'''

print('do another')
time.sleep(10)