'''
Created on 13 apr 2017

@author: bossima1
'''
import Team_Management
import MatchEngine
import random

class Tournament:
    numberOf_teams = 0
    def __init__(self):
        self.teams = self.set_teams()
        self.scoreboard = Scoreboard(self)
        self.calendarManagement = calendarManagement(self)       
        
    def set_teams(self):
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
            mEngine = MatchEngine.MatchEngine(tmp_teams[0],tmp_teams[1])
            #result = MatchEngine.matchEngine(tmp_teams[0],tmp_teams[1]).game_ActionsManagement()
            result = mEngine.game_ActionsManagement()
            if(result == 0):
                self.scoreboard.update_TeamScoreboard(tmp_teams[0].TeamName,"D")
                self.scoreboard.update_TeamScoreboard(tmp_teams[1].TeamName,"D")
            elif(result == 1):
                self.scoreboard.update_TeamScoreboard(tmp_teams[0].TeamName,"W")
                self.scoreboard.update_TeamScoreboard(tmp_teams[1].TeamName,"L")   
            elif(result == 2):
                self.scoreboard.update_TeamScoreboard(tmp_teams[0].TeamName,"L")
                self.scoreboard.update_TeamScoreboard(tmp_teams[1].TeamName,"W")                   
##########################################################


class calendarManagement:
    def __init__(self,Tournament):
        tmpTeams = Tournament.teams
        self.ValidCalendar = self.make_schedule(Tournament)
    
    def printDayMatches(self,index):
        for i in range(len(self.ValidCalendar[index])):
            print(str(self.ValidCalendar[index][i]))
            
    def printCombinations(self):
        for i in range(len(self.matchesMatrix)):
            print(self.matchesMatrix[i])
    
    def printCalendar(self):
        for i in range(len(self.ValidCalendar)):
            print(str(self.ValidCalendar[i]))


    def make_day(self,Tournament, day):
        num_teams = Tournament.numberOf_teams
        # using circle algorithm, https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
        assert not num_teams % 2, "Number of teams must be even!"
        # generate list of teams
        lst = Tournament.teams
        # rotate
        day %= (num_teams - 1)  # clip to 0 .. num_teams - 2
        if day:                 # if day == 0, no rotation is needed (and using -0 as list index will cause problems)
            lst = lst[:1] + lst[-day:] + lst[1:-day]
        # pair off - zip the first half against the second half reversed
        half = num_teams // 2
        return list(zip(lst[:half], lst[half:][::-1]))

    def make_schedule(self,Tournament):
        # number of teams must be even!
        # build first round-robin
        schedule = [self.make_day(Tournament, day) for day in range(Tournament.numberOf_teams - 1)]
        # generate second round-robin by swapping home,away teams
        swapped = [[(away, home) for home, away in day] for day in schedule]
        return schedule + swapped

    
            
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


