class Ranking:
    def __init__(self,leagueName):
        self.leagueID = leagueName
        
    def freshSeason(self,teams : list):
        self.LeagueTable = dict()
        for team in teams:
            self.LeagueTable[team] = {"Days":1,"Points":0,"Wins":0,"Draws":0,"Losses":0}

    def setWin(self,winnerTeam):
        self.LeagueTable[winnerTeam]["Days"] = self.LeagueTable[winnerTeam]["Days"] + 1
        self.LeagueTable[winnerTeam]["Points"] = self.LeagueTable[winnerTeam]["Points"] + 3
        self.LeagueTable[winnerTeam]["Wins"] = self.LeagueTable[winnerTeam]["Wins"] + 1

    def setLoss(self,looserTeam):
        self.LeagueTable[looserTeam]["Days"] = self.LeagueTable[looserTeam]["Days"] + 1
        self.LeagueTable[looserTeam]["Losses"] = self.LeagueTable[looserTeam]["Losses"] + 1

    def setDraw(self,drawerTeam):
        self.LeagueTable[drawerTeam]["Days"] = self.LeagueTable[drawerTeam]["Days"] + 1
        self.LeagueTable[drawerTeam]["Points"] = self.LeagueTable[drawerTeam]["Points"] + 1
        self.LeagueTable[drawerTeam]["Draws"] = self.LeagueTable[drawerTeam]["Draws"] + 1

    def setResult(self,team1,team2,result):     #result = -1 (team1 win) / result = 0 (draw) / result = 1 (team2 win)
        if result == -1:
            self.setWin(team1)
            self.setLoss(team2)
        elif result == 0:
            self.setDraw(team1)
            self.setDraw(team2)
            else:
                self.setLoss(team1)
                self.setWin(team2)
