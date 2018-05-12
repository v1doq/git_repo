import requests
import json
import http.client
get = requests.get("http://www.google.com")
get2 = http.client.HTTPConnection("http://www.google.com: 80")
site = None
if get.status_code == 200:
    site = get.url
print(get, site)
print("______________________________________________________")

#get2 = http.client.HTTPMessage("http://www.google.com: 80")
print(get2)