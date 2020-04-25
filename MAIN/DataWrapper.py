import json
import requests
import Player_Management

baseUrl = "http://localhost:3000/players"
headers = {'Content-type': 'application/json'}

tmp = Player_Management.Player()


toBeloaded = json.dumps(tmp.toJSON())


res = json.loads(tmp.toJSON())

print(res["name"])

