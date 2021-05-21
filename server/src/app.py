import os.path

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

from flask import Flask, render_template, request, make_response

from datetime import datetime, date
app = Flask(__name__)


@app.route('/')
def index():
    today = date.today()
    copyrightdate = today.strftime('%Y')
    template = render_template("index.html", copyRightDate=copyrightdate)
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    today = date.today()
    copyrightdate = today.strftime('%Y')
    if request.method == "POST":
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive.file',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
        service = discovery.build('sheets', 'v4', credentials=creds)

        # The ID of the spreadsheet to update.
        spreadsheet_id = '1iIzn5m_mw3DaUK7l4HzNNqKhO2n1rwyPLV0yFMB2rk4'  # TODO: Update placeholder value.

        # The A1 notation of a range to search for a logical table of data.
        # Values will be appended after the last row of the table.
        range_ = 'A1'  # TODO: Update placeholder value.

        # How the input data should be interpreted.
        value_input_option = "RAW"  # TODO: Update placeholder value.

        # How the input data should be inserted.
        insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.

        data = request.form.to_dict()
        date_time = datetime.now()
        value_range_body = {
            "values": [
                [
                    data["name"],
                    data["email"],
                    data["message"],
                    date_time.strftime('%b %d, %Y %H:%M')
                ]
            ]
        }

        req = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_,
                                                     valueInputOption=value_input_option,
                                                     insertDataOption=insert_data_option, body=value_range_body)
        req.execute()
        return render_template("index.html", showmodal = True, copyRightDate=copyrightdate)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
