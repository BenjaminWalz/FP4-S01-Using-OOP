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
        return '{} {} {}'.format(self.wins, self.ties, self. losses)
        
      
      
class Player(Team):
    
    def __init__(self, team, first, last, number, wins, losses, ties, goals, assists):
        super().__init__(self, team, wins, losses, ties)
        self.team = team
        self.number = number
        self.first = first
        self.last = last
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
          
    def Player_Profile(self):
        return '{} {} {} {}'.format(self.first, self.last, self.number, self.points)
    
 
 
# location = input("Where is the team from? ")
# team = input("What is the team name? ")
# team = Team(team, location, 0, 0, 0)
# print(team.Team_Location())
 
 

def main():
    print("""
This program makes and groups either a team with the teams wins, ties and losses,
or a player with they're name, number, goals and assits with total points.
""")
    choice = int(input("Do you want to group a player(1) or a team(2) "))
    if choice == 1:
        print("list the following info")
        team = input("What is the team name> ")
        first = input("What is the players first name> ")
        last = input("What is the players last name> ")
        number = input("What number is the player> ")
        number = '#' + number
        goals = int(input("How many goals does your player have> "))
        assists = int(input("How many assists does your player gave> "))
        player = Player(team, first, last, number, 0, 0, 0, goals, assists)
        print(player.Player_Profile())
        
main()
        



        
        
