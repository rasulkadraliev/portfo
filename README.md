# portfo
This is code for my portfolio web-site www.kadraliev.com. Used Flask application and integration with Google Sheets API

The code is in Docker container on Cloud Run which is created via terminal command:
gcloud builds submit --tag gcr.io/portfo-98f38/portfo
gcloud beta run deploy --image gcr.io/portfo-98f38/portfo

and then it's deployed to Firebase with terminal command: firebase deploy