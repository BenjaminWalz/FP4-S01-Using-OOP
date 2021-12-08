class Team:
    
    def __init__(self, team, location, wins, losses, ties,):
        self.team = team
        self.location = location
        self.wins = wins
        self.losses = losses
        self.ties = ties
   
    def Team_Location(self):
        return '{} {}'.format(self.location, self.team)
        
    def Record(self):
        self.record = self.wins, self.losses, self.ties
        
      
      
class Player(Team):
    def __init__(self, team, number, wins, losses, ties):
        super().__init__(team, wins, losses, ties)
      # this above dont work ben
      
      
      
      
      
team = Player('Wheat Kings', 'West Central', 10, 8, 2)


print(team.Team_Location())
print(team.Record())


        
        
