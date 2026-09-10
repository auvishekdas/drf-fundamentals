import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'id' : 1,
    'student_name' : 'Limon',
    'class_name' : 'Ten',
    'seat' : 48,
}
json_data = json.dumps(data)
r = requests.put(url = URL, data = json_data)
print(r.json())