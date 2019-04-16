import operator

class Team:
    def __init__(self, name, wins, losses, draws, points = 0):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = points
        self.points += wins*3 + draws*1
        self.matches_played = 0
        self.matches_played += self.wins + self.losses + self.draws

    def addScores(self, win = 0, loss = 0, draw = 0):
        self.wins += win
        self.losses += loss
        self.draws += draw
        self.points += win*3 + draw*1
        self.matches_played += 1

def getOrderedTeamList (dict):
    teams = []
    for team in dict.keys():
        teams.append((team, dict[team].points))
    ordered_teams = sorted(sorted(teams, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)
    return ordered_teams

def tally(tournament_results):

    results = "Team" + ((31-len("Team")) * " ") + "| MP |  W |  D |  L |  P\n"

    if tournament_results == '':
        return results[:-1]

    tournament_results = tournament_results.split("\n")
    teams = {}

    for game in tournament_results:
        data = game.split(";")
        team1 = data[0]
        team2 = data[1]
        game_res = data[2]
        temp_dict = {}
        if game_res == "win":
            temp_dict[1] = [team1,1,0,0]
            temp_dict[2] = [team2,0,1,0]
        elif game_res == "loss":
            temp_dict[1] = [team1,0,1,0]
            temp_dict[2] = [team2,1,0,0]
        elif game_res == "draw":
            temp_dict[1] = [team1,0,0,1]
            temp_dict[2] = [team2,0,0,1]

        if team1 not in teams:
            teams[team1] = Team(name = temp_dict[1][0], wins = temp_dict[1][1], losses = temp_dict[1][2], draws = temp_dict[1][3])
        else:
            teams[team1].addScores(temp_dict[1][1], temp_dict[1][2], temp_dict[1][3])

        if team2 not in teams:
            teams[team2] = Team(name = temp_dict[2][0], wins = temp_dict[2][1], losses = temp_dict[2][2], draws = temp_dict[2][3])
        else:
            teams[team2].addScores(temp_dict[2][1], temp_dict[2][2], temp_dict[2][3])

    ordered_teams = getOrderedTeamList(teams)

    for team_temp in ordered_teams:
        team = team_temp[0]
        results += teams[team].name + ((30 - len(teams[team].name)) * " ") + " |  " + str(teams[team].matches_played) + " |  " + str(teams[team].wins) + " |  " + str(teams[team].draws) + " |  " + str(teams[team].losses) + " |  " + str(teams[team].points) + "\n"

    return results [:-1]
