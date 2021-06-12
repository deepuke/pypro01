from flask.globals import request
import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {'views': 110, 'name':'Tim', 'likes':65}, 
    {'views': 5410, 'name':'abc', 'likes':690}, 
    {'views': 120, 'name':'pqr', 'likes':2316}
]

for i in range(len(data)):
    response = requests.put(BASE+"video/"+ str(i), data[i])
    print(response.json())

response = requests.delete(BASE+"video/0")
print(f"{response.status_code} and {response}")

input()

response = requests.get(BASE+"video/2")
print(response.json())