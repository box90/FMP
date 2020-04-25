import utils
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

    def createPlayer(self):
        self.Values = dict()
        self.nationality = utils.Utils().getNation()
        self.name = utils.Utils().getName(self.nationality)
        self.surname = utils.Utils().getSurname(self.nationality)
        self.birthDate = utils.Utils().getDate().strftime("%d/%m/%Y")
        
        #assign attributes
        for i in utils.Utils().AttributeType:
            self.Values[i] = random.randint(0,20)
        #self.role = InfoManagement.setValidPosition(self)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)