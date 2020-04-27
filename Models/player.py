import utils
import utils_player
import random
import json

class Player:
    #def __init__(self):
    #    pass
    
    def __init__(self,**kwargs):
        self.Values = kwargs.get('Values')
        self.nationality = kwargs.get('nationality')
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.birthDate = kwargs.get('birthDate')
        self.role = kwargs.get('role')
        self.teamID = kwargs.get('teamID')

    def createPlayer(self):
        self.Values = dict()
        self.nationality = utils.Utils().getNation()
        self.name = utils.Utils().getName(self.nationality)
        self.surname = utils.Utils().getSurname(self.nationality)
        self.birthDate = utils.Utils().getDate().strftime("%d/%m/%Y") 
        #assign attributes
        for i in utils.Utils().AttributeType:
            self.Values[i] = random.randint(0,20)
        #assign role
        self.setRole()

    def setRole(self):
        self.role = utils_player.setValidPosition(self.Values)


    def developPlayerToRole(self,role):
        self.role = role
        self.Values = utils_player.forceRoleAttribute(role)
    
    def setTeam(self,teamID):
        self.teamID = teamID