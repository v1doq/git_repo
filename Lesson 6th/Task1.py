import requests

site = "http://pulse-rest-testing.herokuapp.com/roles/"
payload = {"name": "Dima", "type": "home", "book": "1"}
payload2 = {"name": "Dmitry", "type": "IDDQD", "book": "99"}
response = requests.post(site, payload)
response = response.json()
id = str(response["id"])
new_site = site + id
r = requests.get(new_site)
if r.status_code == 200:
    print("Object has been created")
else:
    print(r)
r2 = requests.get(site)

if r.json() in r2.json():
    print("Object is present in roles")
else:
    print("Something wrong with request")
r3 = requests.put(new_site, payload2)

if r3.status_code == 200:
    print("Object has been changed")
else:
    print(r3)
r4 = requests.get(new_site)
if r3.json() in r4.json():
    print("Object is present in roles")
else:
    print("Something wrong with request")
r5 = requests.delete(new_site)
print(r.text)

print(response, " ID: ", id)
