'''
Created on 13 apr 2017

@author: bossima1
'''
from TeamsClasses import Team_Management
from Matches_Management import MatchEngine
import random

class Tournament:
    numberOf_teams = 0
    def __init__(self):
        self.teams = Tournament.set_teams()
        self.scoreboard = Scoreboard(self)
        self.calendarManagement = calendarManagement(self)       
        
    def set_teams():
        listT = []
        for i in range(20):
            listT.append(Team_Management.Team())
            Tournament.numberOf_teams += 1
        return listT

    def search_Team(self,TeamName):
        for i in range(len(self.teams)):
            if(self.teams[i].TeamName == TeamName):
                return self.teams[i]
        
    def get_Team(self,index):
        return self.teams[index]
    
    def print_Calendar(self,index):
        self.calendarManagement.printDayMatches(index)
        
    def playDay(self,index):
        tmp_teams = []
        for i in range(len(self.calendarManagement.ValidCalendar[index])):
            tmp_teams = self.calendarManagement.ValidCalendar[index][i]
            result = MatchEngine.matchEngine(self.search_Team(tmp_teams[0]),self.search_Team(tmp_teams[1])).game_ActionsManagement()
            if(result == 0):
                self.scoreboard.update_TeamScoreboard(tmp_teams[0],"D")
                self.scoreboard.update_TeamScoreboard(tmp_teams[1],"D")
            elif(result == 1):
                self.scoreboard.update_TeamScoreboard(tmp_teams[0],"W")
                self.scoreboard.update_TeamScoreboard(tmp_teams[1],"L")   
            elif(result == 2):
                self.scoreboard.update_TeamScoreboard(tmp_teams[0],"L")
                self.scoreboard.update_TeamScoreboard(tmp_teams[1],"W")                   
##########################################################


class calendarManagement:
    def __init__(self,Tournament):
        self.matchesMatrix = [[0 for x in range(Tournament.numberOf_teams + 1)] for y in range(Tournament.numberOf_teams + 1)]
        for i in range(0,Tournament.numberOf_teams):
            self.matchesMatrix[i+1][0] = Tournament.get_Team(i).TeamName
            self.matchesMatrix[0][i+1] = Tournament.get_Team(i).TeamName
            self.matchesMatrix[i][i] = 1
        self.matchesMatrix[Tournament.numberOf_teams][Tournament.numberOf_teams] = 1
        
        for i in range(1,len(self.matchesMatrix)):
            for j in range(i,len(self.matchesMatrix)):
                self.matchesMatrix[i][j] = 1
        
        #print empty calendar
        #for i in range(len(self.matchesMatrix)):
        #    print(self.matchesMatrix[i])
        
        self.ValidCalendar = []
        #while(len(self.ValidCalendar) < (((Tournament.numberOf_teams*2)-2)/2)):
        #    self.ValidCalendar.append(calendarManagement.set_correctMatches(self, Tournament))
        #    print("Creata giornata: " + str(len(self.ValidCalendar))) 
        self.ValidCalendar = calendarManagement.set_correctMatches(self,Tournament)

    
    def set_correctMatches(self,Tournament):
        tmp_combinations = []
        #used_valuesX = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        #used_valuesY = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        tmpTeams = Tournament.teams

        while len(tmpTeams) > 0:
            home = random.choice(tmpTeams)
            tmpTeams.pop(tmpTeams.index(home))
            away = random.choice(tmpTeams)
            tmpTeams.pop(tmpTeams.index(away))
            tmp_combinations.append([home,away])
        #for i in range(int(Tournament.numberOf_teams / 2)):
        #    x = random.choice(used_valuesX)
        #    y = random.choice(used_valuesY)
            
        #    while((self.matchesMatrix[x][y] == 1)):
        #        x = random.choice(used_valuesX)
        #        y = random.choice(used_valuesY)
                
        #    self.matchesMatrix[x][y] = 1  
        #    used_valuesX.pop(used_valuesX.index(x))
        #    used_valuesY.pop(used_valuesY.index(y))
             
        #    tmp_combinations.append([self.matchesMatrix[x][0],self.matchesMatrix[0][y]])
        return tmp_combinations
    
    def printDayMatches(self,index):
        for i in range(len(self.ValidCalendar[index])):
            print(str(self.ValidCalendar[index][i]))
            
    def printCombinations(self):
        for i in range(len(self.matchesMatrix)):
            print(self.matchesMatrix[i])
    
    def printCalendar(self):
        for i in range(len(self.ValidCalendar)):
            print(str(self.ValidCalendar[i]))
            
####################################################################
class Scoreboard:
    days = 0
    def __init__(self,Tournament):
        self.tables = []                #[TeamName,giornata,vittorie,pareggi,sconfitte,punti]
        for i in range(Tournament.numberOf_teams): 
            self.tables.append([Tournament.get_Team(i).TeamName,0,0,0,0,0])

    def printScoreboard(self):
        print("[TeamName,Days,W,D,L,Points]")
        for i in range(len(self.tables)):
            print(str(self.tables[i]))

    def get_TeamScoreboard(self,TeamName):
        for i in range(len(self.tables)):
            if(self.tables[i][0] == TeamName):
                return i

    def update_TeamScoreboard(self,TeamName,Result):
        index = Scoreboard.get_TeamScoreboard(self,TeamName)
        tmp_S = self.tables[index]
        
        if(Result == "V"):
            self.tables[index][1] = tmp_S[1] + 1
            self.tables[index][2] = tmp_S[2] + 1
            self.tables[index][5] = tmp_S[3] + 3
        elif(Result == "D"):
            self.tables[index][1] = tmp_S[1] + 1
            self.tables[index][3] = tmp_S[2] + 1
            self.tables[index][5] = tmp_S[4] + 1
        elif(Result == "L"):
            self.tables[index][1] = tmp_S[1] + 1
            self.tables[index][5] = tmp_S[5] + 1
            
##########################################            