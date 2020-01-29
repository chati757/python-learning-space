from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

"""
example spreadsheet link : https://docs.google.com/spreadsheets/d/1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4/edit?folder=1PNzfBKYntkb14Dv3dzoOXNPPkgEDiM88#gid=534433466
example sheet : test_api
#ref :
step to create oauth2 for use in google spreadsheet : https://developers.google.com/adwords/api/docs/guides/authentication#webapp
example code (quick start) : https://developers.google.com/sheets/api/quickstart/python
example read and write : https://developers.google.com/sheets/api/guides/values
"""

#https://console.cloud.google.com/apis/credentials?project=project-deeptune
#get from secret file of oauth2 (in topic oauth2.0 client ids , see the list and download some list of that)
credentials = "./auth/credential.json"
api_service_name = 'sheets'
api_version = 'v4'
# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
#type of scope (google sheet api v4) : https://developers.google.com/identity/protocols/googlescopes 

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
#SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SPREADSHEET_ID = '1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4'
SHEET_ID = 534433466
SHEET_NAME = 'test_api'
RANGE_NAME = SHEET_NAME+'!A2'

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    # not creds.valid  เป็นกรณีที่เข้าไปหา token.packle ตาม path แล้วเจอแต่ token เป็นค่าว่าง creds เลยเป็น instance ของ pickle แล้ว เลยสามารถใช้ .valied ได้
    # แต่ถึงแม้ creds เป็นแค่ None และ ไม่ได้เป็น instance ของ pickle condition (if not creds or not creds.valid) ก็ไม่ error แต่อย่างใด อาจเป็นเพราะ if ของ pythonทำมาดี มี except แต่
    # ก็ยังตรวจสอบเงื่อนไข อื่นๆต่อ แล้วทำงานต่อไปได้ โดยปกติ creds.valid ต้อง raise exception ไปแล้วเพราะไม่เป็น instance ของ pickle .valid คงไม่เข้าใจ
    if not creds or not creds.valid:
        #incase creds.valid but creds is instance of pickle
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            #incase no token for credential it's will be create google client secrets file from json client_secret_file [json file]
            flow = InstalledAppFlow.from_client_secrets_file(credentials, SCOPES)
            #run local_server for receive token
            """
            run the flow using the server strategy

            the server strategy instructs the user to open the auth url in thier browser and will attempt to automatically open the url for them.
            it's will start a local web server to listen for the auth response.Once auth is complete the auth server will redirect the user's browser to the
            local web server.The web server will get the authorization code from the response and shutdown. the code is then exchanged for a token.
            """
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run (save token)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try : 
        service = build(api_service_name,api_version, credentials=creds)
        print("service created successfully")
        print(service)
    except Exception as e:
        raise Exception(e)
    
    """
    #basic read
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(values)
    """

    """
    basic write
    target_wr_sheet = {
        'spreadsheet_id':None, #'1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4'
        'range' : None, #'sheetname!A2:A'
        'value_input_option' : 'RAW',
        'body' : {
            'values':[[]] #[["bvaluea1","btest1"], ["bvaluea2"], ["bvaluea3"]]
        }
    }
    result = service.spreadsheets().values().update(spreadsheetId=target_wr_sheet['spreadsheet_id'], range=target_wr_sheet['range'],valueInputOption=target_wr_sheet['value_input_option'], body=target_wr_sheet['body']).execute()
    return ('{0} cells updated.'.format(result.get('updatedCells')))
    """

    """
    #basic append
    # The A1 notation of a range to search for a logical table of data.
    # Values will be appended after the last row of the table.
    range_ = 'my-range'  # TODO: Update placeholder value.

    # How the input data should be interpreted.
    value_input_option = 'RAW'  # TODO: Update placeholder value.

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.

    list_data = [["bvaluea1","btest1"], ["bvaluea2"], ["bvaluea3"]]
    value_range_body = {
        "majorDimension": "ROWS",
        "values": list_data
    }
    
    sheet = service.spreadsheets()
    request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    print(response)
    """

    """
    #insert row and shift
    spreadsheet_id = '1z6yPdxy3MSOUo1QESUkoyqSyDtzSftdoRddFtRVQeo4'
    batch_update_spreadsheet_request_body = {
        "requests": [
            {
                "insertRange": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "startRowIndex": 1,
                        "endRowIndex": 2
                    },
                    "shiftDimension": "ROWS"
                }
            },
            {
                "pasteData": {
                    "data": "=B1, 444, 222",
                    "type": "PASTE_NORMAL",
                    "delimiter": ",",
                    "coordinate": {
                        "sheetId": SHEET_ID,
                        "rowIndex": 1
                    }
                }
            }
        ]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
    response = request.execute()
    print(response)
    """

if __name__ == '__main__':
    main()