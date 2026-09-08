import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'student_name' : 'Hasan Karim',
    'class_name' : 'Nine',
    'seat' : 55
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)