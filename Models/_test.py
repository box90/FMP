import random
import names 
import faker
import utils
import player
import json
from utils_player import player_to_dict
from utils_player import dict_to_player
from utils_tournament import tournament_to_dict
from utils_tournament import dict_to_tournament
import team
import tournament
import pprint

tour = tournament.Tournament("SerieA",10)
tour.inizializeTeams([  "Team1",
                        "Team2",
                        "Team3",
                        "Team4",
                        "Team5",
                        "Team6",
                        "Team7",
                        "Team8",
                        "Team9",
                        "Team10"])

tour.createCalendar()
data = json.dumps(tour,default=tournament_to_dict, sort_keys=True)
with open('Tournament.json', 'w') as outfile:
    outfile.write(data)
#pprint.pprint(data)

#TeamTest
#t = team.Team()
#t.createTeam("Pippoli")

#PlayerTest
#p = player.Player()
#p.createPlayer()
#print(json.dumps(p,default=player_to_dict,indent=4, sort_keys=True))

#serialize
#data = json.dumps(p,default=player_to_dict,indent=4, sort_keys=True)
#print(data)

#deserialize
#d = json.loads(data,object_hook=dict_to_player)
#print(type(d))