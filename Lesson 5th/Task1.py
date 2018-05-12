import requests

id = {"id": "57"}
r = requests.get("http://pulse-rest-testing.herokuapp.com/roles/", id)
print(r.text)
payload = {"name": "Dima", "type": "home", "level": "80", "book": "13"}
#r = requests.post("http://pulse-rest-testing.herokuapp.com/roles/", payload)
#print(r)
r = r.json()
last = dict(r[-1])
#id = last.items()
id = last.get("id")
if "Dima" in last.get("name") and "home" in last.get("type"):
    print("sdfdsfsdafas")
print(id)
print(dict.items(last))