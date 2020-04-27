import utils
import random

attribute_role_mapping = {
            'Shoot': ['CM','LM','RM','ST'],
            'Tackle': ['DC','DL','DR','CM'],
            'Pass': ['CM','LM','RM','AM'],
            'Aerial ability': ['GK','DC','CM','ST'],
            'Dribling': ['RM','LM','ST'],
            'Free Kick': ['ES','ST'],
            'Speed': ['GK','DR','DL','LM','RM'],
            'Stamina': ['DR','DL','LM','RM'],
            'Finishing': ['ES','ST'],
            'Mental': ['DC','DR','DL']
        }


#FUNCTIONS
#serialization/deserialization
def player_to_dict(obj):
        #  Populate the dictionary with object meta data 
        obj_dict = {

        }
        
        #  Populate the dictionary with object properties
        obj_dict.update(obj.__dict__)
  
        return obj_dict



def dict_to_player(our_dict):
    class_name = "Player"
    module_name = "player"
    module = __import__(module_name)
    class_ = getattr(module,class_name)
    obj = class_(**our_dict)

    return obj



def setValidPosition(player_attributes : dict):
        #set positionChecker
        positionChecker = dict()
        for i in utils.Utils().positions:
            positionChecker[i] = 0

        ################################################
        for p_a in player_attributes:
            name2check  = p_a
            value2check = player_attributes[p_a]
            
            if value2check >= 10:
                validRoles = attribute_role_mapping[name2check]
                for p in validRoles:
                    positionChecker[p] = positionChecker[p] + random.randint(1,3)
        ##################################################
           
        #print(str(positions))
        potential_pos = []
        max_pos = max(positionChecker, key=positionChecker.get)
        max_value = positionChecker.get(max_pos)
        
        for key in positionChecker:
            if(positionChecker.get(key) == max_value):
                potential_pos.append(key)

        valid_pos = random.choice(potential_pos)
        
        #print(str(valid_pos))
        return valid_pos       


def forceRoleAttribute(role):
    forcedAttribute = dict()
    for x in attribute_role_mapping:
        if role in attribute_role_mapping[x]:
            forcedAttribute[x] = random.randint(9,15)
        else:
            forcedAttribute[x] = random.randint(1,10)
    
    return forcedAttribute