def make_day(tournamentTeams: dict, day):
        num_teams = len(tournamentTeams)
        # using circle algorithm, https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
        assert not num_teams % 2, "Number of teams must be even!"
        # generate list of teams
        lst = list(tournamentTeams.keys())
        # rotate
        day %= (num_teams - 1)  # clip to 0 .. num_teams - 2
        if day:                 # if day == 0, no rotation is needed (and using -0 as list index will cause problems)
            lst = lst[:1] + lst[-day:] + lst[1:-day]
        # pair off - zip the first half against the second half reversed
        half = num_teams // 2
        return list(zip(lst[:half], lst[half:][::-1]))

def make_schedule(tournamentTeams : dict):
    # number of teams must be even!
    # build first round-robin
    # ,0 rapresent result of the match 
    schedule = [make_day(tournamentTeams, day) for day in range(len(tournamentTeams) - 1)]
    # generate second round-robin by swapping home,away teams
    scheduleWithResult = [[((home, away),0) for home, away in day] for day in schedule]
    swapped = [[((away, home),0) for home, away in day] for day in schedule]
    return scheduleWithResult + swapped
