import utils
import player

valid_formation = dict([('GK',1),('DC',2),('DL',1),('DR',1),('CM',2),('LM',1),('RM',1),('ST',2)])

#FUNCTIONS
#serialization/deserialization
def team_to_dict(obj):
        #  Populate the dictionary with object meta data 
        obj_dict = {

        }
        
        #  Populate the dictionary with object properties
        obj_dict.update(obj.__dict__)
  
        return obj_dict



def dict_to_team(our_dict):
    class_name = "Team"
    module_name = "team"
    module = __import__(module_name)
    class_ = getattr(module,class_name)
    obj = class_(**our_dict)

    return obj



def createValidTeam():
    current_formation = dict([('GK',[]),('DC',[]),('DL',[]),('DR',[]),('CM',[]),('LM',[]),('RM',[]),('ST',[])])
    
    #main procedure -- Fill current_formation
    team = 0
    while(team == 0):
        tmp_player = player.Player()
        tmp_player.createPlayer()

        if(tmp_player.role == 'AM' or tmp_player.role == 'ES'):
            continue    #skip useless position

        if(len(current_formation[tmp_player.role]) >= valid_formation[tmp_player.role]):
            continue    #skip full role
            
        current_formation[tmp_player.role].append(tmp_player)

        if(all(len(current_formation[k])>=valid_formation[k] for k in current_formation)):
            team = 1
        else:
            team = 0
    
    return current_formation

    
def forceValidTeam(teamID):
    current_formation = dict([('GK',[]),('DC',[]),('DL',[]),('DR',[]),('CM',[]),('LM',[]),('RM',[]),('ST',[])])

    for r in valid_formation:
        while(len(current_formation[r]) < valid_formation[r]):
            tmp_player = player.Player()
            tmp_player.createPlayer()
            tmp_player.setTeam(teamID)
            tmp_player.developPlayerToRole(r)

            current_formation[r].append(tmp_player)

    return current_formation
            