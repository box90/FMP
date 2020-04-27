import random
import team
import utils_team
import utils_calendar
import scoreboard

class Tournament:
    def __init__(self,name,numberOfTeams):
        self.name = name
        self.numberOfTeams = numberOfTeams
        self.myTeams = dict()

    def createAndAppendTeam(self,teamName):
        tmp_team = team.Team()
        tmp_team.createTeam(teamName)
        self.myTeams[teamName] = tmp_team

    def inizializeTeams(self,teamsNames):
        for teamName in teamsNames:
            self.createAndAppendTeam(teamName)

    def createCalendar(self):
        self.Calendar = utils_calendar.make_schedule(self.myTeams)

    def createRanking(self):
        self.Ranking = scoreboard.Ranking(self.name)
        self.Ranking.freshSeason(list(self.myTeams.keys()))