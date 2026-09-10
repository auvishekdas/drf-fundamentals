import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'id' : 3,
}

json_data = json.dumps(data)
r = requests.delete(url = URL, json = data) 
print("Status Code:", r.status_code )
data = r.json()
print(data)