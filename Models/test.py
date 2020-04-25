import random
import names 
import faker
import utils
import player
import json
from serialization import obj_to_dict
from serialization import dict_to_obj


p = player.Player()

#serialize
p.createPlayer()
data = json.dumps(p,default=obj_to_dict,indent=4, sort_keys=True)
print(data)


#deserialize
d = json.loads(data,object_hook=dict_to_obj)
print(type(d))