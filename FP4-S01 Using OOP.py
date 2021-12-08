class Team:
    
    def __init__(self, team_name, location, wins, losses, ties,):
        self.team_name = team_name
        self.location = location
        self.wins = wins
        self.losses = losses
        self.ties = ties
   
    def Team_Location(self):
        return '{} {}'.format(self.location, self.team_name)
        
    def Record(self):
        return '{} {} {}'.format(self.wins, self.losses, self.ties)
        
        
team = Team('Wheat Kings', 'West Central', '10,', '8,', '2')


print(team.Team_Location())
print(team.Record())
        
        
