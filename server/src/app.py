import os.path
from google_sheets_api import *
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
    # Create a variable for template date for copyright in footer
    today = date.today()
    copyrightdate = today.strftime('%Y')

    if request.method == "POST":
        # The ID of the spreadsheet to update.
        spreadsheet_id = '1iIzn5m_mw3DaUK7l4HzNNqKhO2n1rwyPLV0yFMB2rk4'

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
        google_sheets_api(spreadsheet_id, value_range_body)
        return render_template("index.html", showmodal=True, copyRightDate=copyrightdate)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
