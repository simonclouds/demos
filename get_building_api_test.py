import requests

url = "http://www.xxx.me/rest/geography/buildings"

querystring = {"_tl":"3042351012343112","school":"19001"}

headers = {
    'cache-control': "no-cache"
    }

for i in range(1,100):
    response = requests.request("GET", url, headers=headers, params=querystring)
    print i, response.text
    
