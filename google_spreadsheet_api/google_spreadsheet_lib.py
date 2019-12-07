import time
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

service = None

'''
connection = {
    'credentials':None,#credentials oauth2 path (screts.file)
    'scopes':['https://www.googleapis.com/auth/spreadsheets'],
    'api_service_name':'sheets',
    'api_version':'v4'
}
'''
def build_connection(connection):
    global service
    count_try = 1
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

'''
target_wr_sheet = {
    'spreadsheet_id':None, #'1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4'
    'range' : None, #'sheetname!A2:A'
    'value_input_option' : 'RAW',
    'body' : {
        'values':[[]] #[["bvaluea1","btest1"], ["bvaluea2"], ["bvaluea3"]]
    }
}
'''

def write_row(target_wr_sheet):
    count_try = 1
    result = None
    result = target_wr_sheet['service'].spreadsheets().values().update(spreadsheetId=target_wr_sheet['spreadsheet_id'], range=target_wr_sheet['range'],valueInputOption=target_wr_sheet['value_input_option'], body=target_wr_sheet['body']).execute()
    return(result)

'''
#use for insert_row_and_shift_previos_row only 
target_arspr_spreadsheet = {
    'spreadsheet_id':None, #'1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4'
    'sheet_id':None,
    'start_row_index':None, #start index shift row
    'end_row_index':None, #end index shift row
    'data':None, #"=B1, 444, 222"
    'paste_data_row_index':None
}
'''

def insert_row_and_shift_previos_row(target_arspr_spreadsheet):
    response = None
    count_try = 1
    batch_update_spreadsheet_request_body = {
        "requests": [
            {
                "insertRange": {
                    "range": {
                        "sheetId": target_arspr_spreadsheet['sheet_id'],
                        "startRowIndex": target_arspr_spreadsheet['start_row_index'],
                        "endRowIndex": target_arspr_spreadsheet['end_row_index']
                    },
                    "shiftDimension": "ROWS"
                }
            },
            {
                "pasteData": {
                    "data": target_arspr_spreadsheet['data'],
                    "type": "PASTE_NORMAL",
                    "delimiter": ",",
                    "coordinate": {
                        "sheetId": target_arspr_spreadsheet['sheet_id'],
                        "rowIndex": target_arspr_spreadsheet['paste_data_row_index']
                    }
                }
            }
        ]
    }

    request = target_arspr_spreadsheet['service'].spreadsheets().batchUpdate(spreadsheetId=target_arspr_spreadsheet['spreadsheet_id'], body=batch_update_spreadsheet_request_body)
    response = request.execute()
            
    return response

def try_if_error(func,obj_args,trying=5,delay=5,bypass=False):
    count_try = 1
    result = None
    while(True):
        try:
            if(obj_args!=None):
                result = func(obj_args)
            else:
                result = func()
            break
        except Exception as e:
            if(count_try>=trying):
                if(bypass==False):
                    raise Exception(e)
                else:
                    result = None
                    break
            else:
                print('error and retrying')
                count_try += 1
                time.sleep(delay)
                continue
    return result


if __name__ == '__main__':
    print('test main')
    connection = {
        'credentials':'./auth/credential.json',#credentials oauth2 path (screts.file)
        'scopes':['https://www.googleapis.com/auth/spreadsheets'],
        'api_service_name':'sheets',
        'api_version':'v4'
    }
    service = try_if_error(build_connection,connection,5,5)
    print('build success')
    target_wr_sheet = {
        'service':service,
        'spreadsheet_id':'1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4',
        'range' : 'test_api!A2', #'sheetname!A2:A'
        'value_input_option' : 'RAW',
        'body' : {
            'values':[["bvaluea1","btest1"], ["bvaluea2"], ["bvaluea3"]] #[["bvaluea1","btest1"], ["bvaluea2"], ["bvaluea3"]]
        }
    }
    print(try_if_error(write_row,target_wr_sheet,5,5))