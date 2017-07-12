'''
Created on 13 apr 2017

@author: bossima1
'''
from PlayerClasses import Player_Management


class Team:
    counterTeams = 0
    def __init__(self):
        #self.players = Team.set_FirstTeam()
        self.players = Team.create_valid_Team()
        Team.counterTeams += 1
        self.counterPlayers = len(self.players)
        self.TeamName = "Team"+str(Team.counterTeams)

    def set_FirstTeam():
        first_team = []
        for i in range(11):
            first_team.append(Player_Management.Player())
        return first_team

    def create_valid_Team():
        #set dictionary to check
        valid_formation = dict([('GK',1),('DC',2),('DL',1),('DR',1),('CM',2),('LM',1),('RM',1),('ST',2)])
        current_formation = dict([('GK',0),('DC',0),('DL',0),('DR',0),('CM',0),('LM',0),('RM',0),('ST',0)])
        tmp_team = []
        #main procedure
        team = 0
        while(team == 0):
            tmp_player = Player_Management.Player()
            #print(tmp_player.name + ": " + tmp_player.role)
            if(tmp_player.role == 'AM' or tmp_player.role == 'ES'):
                continue    #skip useless position
            
            tmp_value = current_formation.get(tmp_player.role)
            if(tmp_value >= valid_formation.get(tmp_player.role)):
                continue
            
            tmp_value += 1
            current_formation[tmp_player.role] = tmp_value

            if(all(current_formation[k]>=valid_formation[k] for k in current_formation)):
                team = 1
            else:
                team = 0

            tmp_team.append(tmp_player)
            #print(str(current_formation))
            #print(str(valid_formation))
        return tmp_team

    def prinTeam(self):
        print("##"+self.TeamName+"##")
        print("#####################")
        for i in range(len(self.players)):
            self.players[i].printPlayer()
            print("")
        print("#####################")
        print("Number of players: " + str(self.counterPlayers))    

#######################################
    def getPlayer(self,position):
        for i in range(len(self.players)):
            if(self.players[i].role == position):
                return self.players[i]
