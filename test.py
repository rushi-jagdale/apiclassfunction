import requests

BASE_URL = "http://127.0.0.1:8000/jsonapi"
res = requests.delete(BASE_URL)
data = res.json()
print(data)
# print('eno:',data['eno'])
# print('name:',data['name'])