import requests

response = requests.get('http://127.0.0.1:8000/drink_list/')

print(response.json())