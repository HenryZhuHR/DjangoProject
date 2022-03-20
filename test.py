# encoding:utf-8

import json
import requests

request_url = "http://127.0.0.1:8000"


payload = json.dumps({
    # "name": "test"
})
request_url = request_url + "/api/post"
headers = {
   'Content-Type': 'application/json'
}
response = requests.post(
    request_url,
    data=payload,
    headers=headers
)
print(response.json())
