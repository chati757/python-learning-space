import time
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def build_connection(connection):
    global service
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        #incase creds.valid but creds is instance of pickle
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            #incase no token for credential it's will be create google client secrets file from json client_secret_file [json file]
            flow = InstalledAppFlow.from_client_secrets_file(connection['credentials'],connection['scopes'])
            #run local_server for receive token
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run (save token)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build(connection['api_service_name'],connection['api_version'], credentials=creds)
            
    return service