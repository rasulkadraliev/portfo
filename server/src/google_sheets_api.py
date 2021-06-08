from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

def google_sheets_api(spreadsheet_id, value_range_body):

    # Google API requirement to define the scope of access
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']

    # Use creds to create a client to interact with the Google Drive API
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    service = discovery.build('sheets', 'v4', credentials=creds)

    # The A1 notation of a range to search for a logical table of data.
    # Values will be appended after the last row of the table.
    range_ = 'A1'

    # How the input data should be interpreted.
    value_input_option = 'RAW'

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'

    req = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_,
                                                 valueInputOption=value_input_option,
                                                 insertDataOption=insert_data_option, body=value_range_body)
    req.execute()
    return
