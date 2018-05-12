import requests

r = requests.get("http://pulse-rest-testing.herokuapp.com/books")
payload = {"title": "New_book", "author": "Dmitry"}
new = requests.post("http://pulse-rest-testing.herokuapp.com/books/", payload)
print(r.text, new.status_code)
answer = new.json()
print(answer)