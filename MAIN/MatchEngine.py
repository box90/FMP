'''
Created on 13 apr 2017

@author: bossima1
'''
import Team_Management
import random



class MatchEngine:
    def __init__(self,Team1,Team2):
        self.teamHome = Team1
        self.teamAway = Team2
        self.score = [0,0]

    def FreeKickManagement(self,teamAttack,teamDefend):
        stricker = teamAttack.getPlayer("ST")
        goalKeeper = teamDefend.getPlayer("GK")
        
        rnd_strike = random.randint(1,20) + (random.randint(0,3)*stricker.Values.get_attributeValue("Finalizzazione")) + random.randint(-5,3)
        rnd_goalKeep = random.randint(1,20) + (random.randint(0,4)*goalKeeper.Values.get_attributeValue("Resistenza")) + random.randint(0,5)
        calc_strike = stricker.Values.get_attributeValue("Tiro") + stricker.Values.get_attributeValue("Calci piazzati") + stricker.Values.get_attributeValue("Mentalita'")
        calc_goalKeep = goalKeeper.Values.get_attributeValue("Gioco aereo") + goalKeeper.Values.get_attributeValue("Velocita'") + goalKeeper.Values.get_attributeValue("Mentalita'")
        #print("Strike: " + str((rnd_strike + calc_strike)))
        #print("GoalKeep: " + str((rnd_goalKeep + calc_goalKeep)))
        if((rnd_strike + calc_strike) > (rnd_goalKeep + calc_goalKeep)):
            return 0
        else:
            return 1
        
        
    def get_sideAttack(self,position):
        if("D" in position):
            return random.choice(["DL","DC","DR"])
        elif("M" in position):
            return random.choice(["LM","CM","RM"])
        elif("S" in position):
            return "ST"
        
    def get_possibleExecution(self,position):
        if(position == "DL"):
            return random.choice(["LM","CM"])
        if(position == "DC"):
            return random.choice(["LM","CM","RM"])
        if(position == "DR"):
            return random.choice(["RM","CM"])  
        if(position == "LM"):
            return random.choice(["CM","ST"])
        if(position == "RM"):
            return random.choice(["CM","ST"])
        if(position == "CM"):
            return random.choice(["LM","RM","ST"])
        if(position == "ST"):
            return "GK"
        
    
    def get_defenderPlayers(self,teamDefend,attPos,possiblePos):
        defenders = []
        if(possiblePos == "LM"):
            defenders.append(teamDefend.getPlayer("RM"))
        elif(possiblePos == "RM"):
            defenders.append(teamDefend.getPlayer("LM"))
        elif(possiblePos == "CM"):
            defenders.append(teamDefend.getPlayer("CM"))
        elif(possiblePos == "ST"):
            defenders.append(teamDefend.getPlayer("DC"))
            if(attPos == "CM"):
                defenders.append(teamDefend.getPlayer("DC"))
            elif(attPos == "LM"):
                defenders.append(teamDefend.getPlayer("DR"))
            elif(attPos == "RM"):
                defenders.append(teamDefend.getPlayer("DL"))
        elif(attPos == "ST"):
            defenders.append(teamDefend.getPlayer("GK"))        
        return defenders    
    
    
    def calculate_possibleExecution(self,teamAttack,teamDefend,nowPos,possiblePos):
        playerAttack = teamAttack.getPlayer(nowPos)
        playersDefend = MatchEngine.get_defenderPlayers(self,teamDefend,nowPos,possiblePos)
        
        #calculate possibilities       
        if(("D" in nowPos) or ("M" in nowPos)):
            rnd_att = random.randint(1,20) + (random.randint(0,3)*playerAttack.Values.get_attributeValue("Passaggi")) + random.randint(-5,3)
            calc_att = playerAttack.Values.get_attributeValue("Dribbling") + playerAttack.Values.get_attributeValue("Velocita'") + playerAttack.Values.get_attributeValue("Mentalita'")    
            rnd_def = calc_def = 0
            for playerDefend in playersDefend: 
                rnd_def += (random.randint(0,4)*playerDefend.Values.get_attributeValue("Contrasti")) + random.randint(-5,5)
                calc_def += playerDefend.Values.get_attributeValue("Resistenza") + playerDefend.Values.get_attributeValue("Velocita'") + playerDefend.Values.get_attributeValue("Mentalita'")
        elif(nowPos == "ST"):
            rnd_att = random.randint(1,20) + (random.randint(0,3)*playerAttack.Values.get_attributeValue("Finalizzazione")) + random.randint(-5,3)
            calc_att = playerAttack.Values.get_attributeValue("Tiro") + playerAttack.Values.get_attributeValue("Mentalita'")
            rnd_def = calc_def = 0
            for playerDefend in playersDefend:
                rnd_def = random.randint(1,20) + (random.randint(0,4)*playerDefend.Values.get_attributeValue("Resistenza")) + random.randint(0,5)
                calc_def = playerDefend.Values.get_attributeValue("Gioco aereo") + playerDefend.Values.get_attributeValue("Velocita'") + playerDefend.Values.get_attributeValue("Mentalita'")
            
        if((rnd_att + calc_att) > (rnd_def + calc_def)):
            if(nowPos == "ST"):
                return 0
            else:   
                return 1
        else:
            return -1

        
    def AttackManagement(self,teamAttack,teamDefend,position):
        side = MatchEngine.get_sideAttack(self,position)
        possible_exec = MatchEngine.get_possibleExecution(self,side)
        result_exec = MatchEngine.calculate_possibleExecution(self,teamAttack, teamDefend,side,possible_exec)
          
        if(result_exec < 0):
            return -1
        elif(result_exec == 0):
            return 0
        elif(result_exec == 1):
            return MatchEngine.AttackManagement(self,teamAttack, teamDefend,possible_exec)
        
    
      
       
    def flowAction_Start(self,type):    # 0<x<4 attackHome / 4<x<8 attackAway / 9 freeKickHome / 10 freeKickAway
        if(type > 7):
            if(type == 9):
                if(MatchEngine.FreeKickManagement(self,self.teamHome,self.teamAway) == 0):
                    self.score[0] += 1
            else:
                if(MatchEngine.FreeKickManagement(self,self.teamAway,self.teamHome) == 0):
                    self.score[1] += 1   
        else:
            if(0 <= type < 4):
                if(MatchEngine.AttackManagement(self,self.teamHome,self.teamAway,random.choice(["D","M","S"])) == 0):
                    self.score[0] += 1
            else:
                if(MatchEngine.AttackManagement(self,self.teamAway,self.teamHome,random.choice(["D","M","S"])) == 0):
                    self.score[1] += 1  
                
    
    def game_ActionsManagement(self):
        for i in range(random.randint(3,10)):
            MatchEngine.flowAction_Start(self,random.randint(0,9))
        if(self.score[0] > self.score[1]):
            return 1
        elif(self.score[0] < self.score[1]):
            return 2
        elif(self.score[0] == self.score[1]):
            return 0    
                 
        
    def print_Score(self):
        print(self.teamHome.TeamName + ": " + str(self.score[0]))
        print(self.teamAway.TeamName + ": " + str(self.score[1]))
                    
                
                
                
                      