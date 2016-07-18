import requests

url = "http://127.0.0.1:8090/resources/group/"

payload = "name=GroupC&location=CD&size=11"
headers = {
    'content-type': "text/plain",
    'cache-control': "no-cache",
    'postman-token': "cdbe795f-3578-e97b-ebeb-19446a516740"
    }

for i in range(1,10000):
    response = requests.request("GET", url, data=payload, headers=headers)
    i = i + 1

print(response.text)
