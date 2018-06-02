
# install : python3 -m pip install cryptography
#         : python3 -m pip install jwt
# install visualcppbuildtools_full.exe
#         : python3 -m pip install pycrypto
# edit file
# C:\Users\blackcyber\AppData\Local\Programs\Python\Python35\Lib\site-packages\Crypto\Random\OSRNG\nt.py
#import winrandom ---> from . import winrandom

import requests 
import hashlib
import hmac
import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
import os
'''
{"api key":"DNKQ6FD-940M236-N7QMNDQ-1ZC755Z",
"secret key":"-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAguzR5ESkHdsIWvueREuaG5y0dV2kovTgkVqpgTPS3lkcDrmp/J2bXKfJ\n/oKcbuDQdzuLzE/hLMwsMe5lVtOrEySxipWEyDsF0BvwPNklUmRBfWN9tZzPMspzvYNrdSPW\ngHFP1tvMNJwonkPmx1O+ksmFnzNg/7Hgp5IMGL/otsjvnNj4zi6Vv3KZ4abYGOYIdPpNzSyq\nXmjTVIYJ+M8n3V9K27Hp4rcpjFDbsUERpFo5iMnn+gx7hjtC9pP6X4/VdFfAwUw0ML58jN+k\ntEx3iWxkd/P2Nx4aBrP5fE4yB8RCjxKnmlHMm49nOyr2sa1g6gja3AQ5Ua1qSqEperUaBwID\nAQABAoIBAG8mzT8Fg2uRY/OSQRhsMuaUUKR/nuF2Eh11Igj9zV1Vu7tIpuc/iwHLtXKswlBj\n7rf7RsFrY5kbsb2mTkS7qTa0ZUJpk/RGH7ZBseCG3eeoE+13BOelvEa7mC1hoF4v0dDz4jtg\nGWrk1JsgvJGnKFkIW7f/767E/hxlon10mAZtMF7bNwymhFHAlaJ4HIof1fxm2XGdHFI1elNI\nHDtcpRKSXex0AUdviDxG4vQHYMAydxhjOzHWD7r6ErUJpsvyeIbanhYsgpIyZhMnvoMhA94b\n4Hk23DWOtE4gkUTw4b6YtbN3CFEMpiRwI0VzoLNI3i7Qil5edTo5+ZGAyda8cZECgYEA1cVq\n3S31jpOhIh98jZ94KHC2vC+K1pJioaMtu3kc9IFTNv9bWRKPAEBa7AFyPkcTLPIblYjp0CU9\nFxjF5L6vU7nqIJ/J872RUSH2kYM7j6WII15uMY1IggJyB4IrRm5z0cogfZebev3Amq3K6u2g\nNGBt/McIn2uurkN5BAN0DskCgYEAnMnO5ZiM1kUBSizbPoF9E5ku/SVK7nRHGpP3CYkXkw1Q\n4Blp0DIYtl3zTH25OXue59ci14mOjG+2b+4JN+wUnwDjfew5tlAQz9SUdAk1f5CFZBYBecrl\n7tN+73jFgFFT/b3E/Kz5w+qSMw13Ii7HwoHC6PIPtIbAZ4uPi4izOk8CgYBWc6hsGpIcPwgD\nTMiKXduyPyMnp/J2JG1PATcVgj17hHGq5EqFE0RRzbT3jP4uwX+3xZHyP5SPYP/7v0EI6TTu\nn1lYKEb8E8YZEast3ezQgxkzdJUL5R9VtLd44eOucCzWwu+w2wc+DjE+XNqbd846YGUavUN3\ndY0HXLIsNVlSQQKBgQAJaCI9rDVm9aTqKl7NFT/H2Tz0ezRPsjJB6fa8X7lGXVoo1919XEQX\nTPO39yMRy9Tw2/t/KwWeb2VmucVb0ZI7J/Z+K5oa0hrwHTT68UKAcM9P/fIAuKeq+I15GKng\n1QBRDP2wm0Aw/PXgkkI/jsb1aIulJkDC+AK7M6hdGsqGCQKBgQDEARZ33kK2GnHpYBKmlVl6\nkYm46MY4R0tNJUOSEA0TaZTom6vHNvI6WrVKGr+j7/MblckG12yLIn3nTFSUGzITatHXqbjw\nPC9KnbYsOdAkTOFgS6+PkLxFVqo9u5AIfol1tF6Ke7lNtR3apBIDYiysDX6bVqNgdxJemSke\nspqN7w==\n-----END RSA PRIVATE KEY-----\n"}
'''

public_key_pemfile_path = './public_key.pem'
private_key_pemfile_path = './private_key.pem'


def Main():
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f = open(os.path.abspath(public_key_pemfile_path),"r")
    lines = f.read()
    f.close()
    public_key = '\n'.join(lines.split('\\n'))
    print(public_key)
    
    f = open(os.path.abspath(private_key_pemfile_path),"r")
    lines = f.read()
    f.close()
    private_key = '\n'.join(lines.split('\\n'))
    print(private_key)
    
    '''
    #header
    {
        "alg":"RS256",
        "typ":"JWT"
    }
    #payload
    {
        "some":"payload"
    }
    '''
    jwt.unregister_algorithm('RS256')
    jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))
    encoded = jwt.encode({"some":"payload"},private_key,algorithm='RS256')
    print(encoded)

if __name__=="__main__":
    Main()