'''
Created on 13 apr 2017

@author: bossima1
'''
from TournamentClasses import Tournament_Management
from TeamsClasses import Team_Management
#from PlayerClasses import Player_Management
from Matches_Management import MatchEngine
import random


SerieA = Tournament_Management.Tournament()
#SerieA.calendarManagement.printCombinations()
SerieA.calendarManagement.printCalendar()
print("")
gameDay = 0
SerieA.print_Calendar(gameDay)
print("")
SerieA.playDay(gameDay)
SerieA.scoreboard.printScoreboard()

#matchesMatrix = [[0 for x in range(20)] for y in range(20)]

#for i in range(0,len(matchesMatrix)):
#    for j in range(i,len(matchesMatrix)):
#        matchesMatrix[i][j] = 1
        
#for i in range(len(matchesMatrix)):
#    print(matchesMatrix[i])        