import player
import utils
import utils_team
import random

class Team:
    def __init__(self):
        pass

    def createTeam(self,name):
        self.name = name
        self.myPlayers = utils_team.forceValidTeam(name)