'''
Created on 13 apr 2017

@author: bossima1
'''
import random
import operator
import json
from builtins import str

class InfoManagement:
    def setNation(nat):
        return {
            0:'ITA',
            1:'BRA',
            2:'FRA',
            3:'GER',
            4:'SPA',
            5:'ING',                      
        }[nat]

    def setRole(role):
        return {
            0:'GK',
            1:'DC',
            2:'DL',
            3:'DR',
            4:'CM',
            5:'LM',
            6:'RM',
            7:'AM',
            8:'ES',
            9:'ST',
        }[role]

    def setName(name):
        return {
            0:'Guido',
            1:'Mike',
            2:'Ralph',
            3:'Otto',
            4:'Guillerme',
            5:'Steven',
            6:'Mario',
            7:'Heinz',
            8:'Vincent',
            9:'Luis',
        }[name]

    def setSurname(surname):
        return {
            0:'Ochoa',
            1:'Rossi',
            2:'Von Ribbentrop',
            3:'Gomes',
            4:'Aspas',
            5:'Calabria',
            6:'Connery',
            7:'Mueller',
            8:'Santiago',
            9:'Karaback',
        }[surname]
        
    def setValidPosition(pl):
        positions = dict([('GK',0),('DC',0),('DL',0),('DR',0),('CM',0),('LM',0),('RM',0),('ST',0)])
        
        for i in range(len(pl.Values.Player_attributes)):
            name2check  = pl.Values.Player_attributes[i].get_name()
            value2check = pl.Values.Player_attributes[i].get_value()
            
            #ability check
            if(name2check == "Tiro" and value2check > 5):
                positions['CM'] = positions.get('CM') + 1
                positions['LM'] = positions.get('LM') + 1
                positions['RM'] = positions.get('RM') + 1
                positions['ST'] = positions.get('ST') + 1
                
            elif(name2check == "Contrasti" and value2check > 5):
                #positions['GK'] = positions.get('GK') + 1
                positions['CM'] = positions.get('CM') + 1
                positions['DC'] = positions.get('DC') + 1
                positions['DR'] = positions.get('DR') + 1
                positions['DL'] = positions.get('DL') + 1   
                    
            elif(name2check == "Passaggi" and value2check > 5):
                positions['CM'] = positions.get('CM') + 1
                positions['LM'] = positions.get('LM') + 1
                positions['RM'] = positions.get('RM') + 1 
                
            elif(name2check == "Gioco aereo" and value2check > 5):
                positions['GK'] = positions.get('GK') + 1
                positions['CM'] = positions.get('CM') + 1
                positions['DC'] = positions.get('DC') + 1
                positions['ST'] = positions.get('ST') + 1   
            
            elif(name2check == "Dribbling" and value2check > 5):
                positions['RM'] = positions.get('RM') + 1
                positions['LM'] = positions.get('LM') + 1
                positions['ST'] = positions.get('ST') + 1    
                
            elif((name2check == "Calci piazzati" or name2check == "Finalizzazione") and value2check > 5):
                positions['ST'] = positions.get('ST') + 1          
                    
            elif(name2check == "Velocita'" and value2check > 5):
                positions['GK'] = positions.get('GK') + 1
                positions['DR'] = positions.get('DR') + 1
                positions['DL'] = positions.get('DL') + 1   
                positions['RM'] = positions.get('RM') + 1
                positions['LM'] = positions.get('LM') + 1
                #positions['ST'] = positions.get('ST') + 1  
            
            elif(name2check == "Resistenza" and value2check > 5):
                positions['DR'] = positions.get('DR') + 1
                positions['DL'] = positions.get('DL') + 1 
                positions['RM'] = positions.get('RM') + 1
                positions['LM'] = positions.get('LM') + 1
                
            elif(name2check == "Mentalita'" and value2check > 5):
                positions['DC'] = positions.get('DC') + 1
                positions['DR'] = positions.get('DR') + 1
                positions['DL'] = positions.get('DL') + 1    
            
                
           
        #print(str(positions))
        potential_pos = []
        max_pos = max(positions, key=positions.get)
        max_value = positions.get(max_pos)
        
        for key in positions:
            if(positions.get(key) == max_value):
                potential_pos.append(key)
        
        rnd = random.randint(0,len(potential_pos) -1)
        #print(rnd)
        #print(str(potential_pos))
        
        valid_pos = potential_pos[rnd]
        
        #print(str(valid_pos))
        return valid_pos       
        
                          

class Attribute:
    def __init__(self,name,value):
        self.name = Attribute.f(name)
        self.value = value

    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def f(x):
        return {
            0:'Tiro',
            1:'Contrasti',
            2:'Passaggi',
            3:'Gioco aereo',
            4:'Dribbling',
            5:'Calci piazzati',
            6:"Velocita'",
            7:'Resistenza',
            8:'Finalizzazione',
            9:"Mentalita'",            
        }[x]    

################################
class Attributes:
    def __init__(self):
        self.Player_attributes = []
        for i in range(10):
            self.Player_attributes.append(Attribute(i,random.randint(1,10)))

    def getALL(self):
        for i in range(len(self.Player_attributes)):
            print(self.Player_attributes[i].name +": "+str(self.Player_attributes[i].value))
            
    def get_attributeValue(self,name):
        for i in range(len(self.Player_attributes)):
            if(self.Player_attributes[i].name == name):
                return self.Player_attributes[i].value        
    
##############################
class Player:
    def __init__(self):
        self.Values = Attributes()
        self.name = InfoManagement.setName(random.randint(0,9))
        self.surname = InfoManagement.setSurname(random.randint(0,9))
        self.age = random.randint(18,35)
        self.nationality = InfoManagement.setNation(random.randint(0,5))
        #self.role = InfoManagement.setRole(random.randint(0,9))
        self.role = InfoManagement.setValidPosition(self)

    def printPlayer(self):
        print("Name: "+self.name)
        print("Surname: "+self.surname)
        print("Age: "+str(self.age))
        print("Nationality: "+self.nationality)
        print("Role: "+self.role)
        print("##Attributes##")
        self.Values.getALL()

    def placeHolder(self):
        self.Values = None
        self.name = None
        self.surname = None
        self.age = None
        self.nationality = None
        self.role = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
