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
        self.name = first + ' ' + last
    def Player_Profile(self):
        return '{} {} {} {} {}'.format(self.name, self.number, self.goals, self.assists, self.points)
    
 
 

roster = {}
teams = {}
 

def main():
    print("""
This program makes and groups either a team with the teams wins, ties and losses,
or a player with they're name, number, goals and assits with total points.
""")
    go = True
    while go == True:
        choice = input("Do you want to group a player(1) team(2) or exit(3) ")
        if choice == '1':
            print("list the following info")
            team = input("What is the team name> ")
            first = input("What is the players first name> ")
            last = input("What is the players last name> ")
            number = input("What number is the player> ")
            number = '#' + number
            goals = int(input("How many goals does your player have> "))
            assists = int(input("How many assists does your player have> "))
            points = goals + assists
            player = Player(team, first, last, number, 0, 0, 0, goals, assists)
            add = input("Do you want to add this player to a roster? Yes/No ")
            if add == 'Yes' or add == 'yes':
                name = first + ' ' + last
                stats = player.Player_Profile()
                if team in roster:
                    roster.add(stats)
                    print(roster)
                    
                else:
                    roster[team] = stats
                    print("You added", name)
                    print(roster)
            else:
                print(player.Player_Profile())
            
        elif choice == '2':
            print("list the following info")
            team = input("What is the name of the team> ")
            location = input("Where is the team from> ")
            wins = input("How many wins does the team have> ")
            losses = input("How many losses does the team have> ")
            ties = input("How many ties does the team have> ")
        
        
        
        
        
        
        
        
        
        
        
        
        elif choice == '3':
            print("Thank you, goodbye")
            go = False
        else:
            print("That's not an option")
        
main()
        



        
        
