import json
import requests

baseUrl = "http://localhost:3000/players"
headers = {'Content-type': 'application/json'}

r = requests.get(baseUrl + "?Team=Atalanta")

players = r.json()

realName = "Gomez A."

player = players[0]
player['Name'] = realName

requests.put(baseUrl + "?ID=" + player['ID'], data=json.dumps(player), headers=headers)

