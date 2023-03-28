# snowplow_enrichment_api_dpa
To deploy on cloud run:
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

Example of how to send a request:
```
import requests

url = '<URI of the Cloud Run service with id query string>', #e.g. 'https://enrichment-api-m6dovihfa-ts.a.run.app/user?id=1212'
headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer <your bearer token>'} # get token with `gcloud auth print-identity-token`

response = requests.get(url, headers=headers)
```