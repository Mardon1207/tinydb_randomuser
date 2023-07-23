import requests
from tinydb import TinyDB
from api import url
db = TinyDB('data.json',indent=4)
for i in range(100):
    r=requests.get(url)
    d=r.json()["results"][0]
    db.insert({"first_name":d["name"]["first"],"last_name":d["name"]["last"],"age":d["registered"]["age"],"phone":d["phone"],"email":d["email"]})
    print(i)