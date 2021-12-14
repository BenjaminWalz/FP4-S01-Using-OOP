#Ben Walz
#Using OOP
#Dec 13
#--------






#classes
class Team:
    #init method 
    def __init__(self, team, location, wins, losses, ties,):
        self.team = team
        self.location = location
        self.wins = wins
        self.losses = losses
        self.ties = ties
       #gives the teams name and location when needed and called upon
    def Team_Location(self):
        return '{} {}'.format(self.location, self.team)
        #When called upen gives team record
    def Record(self):
        return '{} {} {} {}'.format(self.team, self.wins, self.ties, self. losses)
        
      
      #inhearrits info from team class
class Player(Team):
    
    def __init__(self, team, first, last, number, wins, losses, ties, goals, assists):
        #calls upon team init method
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
        #gives a list of players detals
        return '{} {} {} {} {}'.format(self.name, self.number, self.goals, self.assists, self.points)
    
 
 
#Dicts
roster = {}
teams = {}
 
#main function
def main():
    print("""
This program makes and groups either a team with the teams wins, ties and losses,
or a player with they're name, number, goals and assits with total points.
""")
    go = True
    while go == True:
        choice = input("Do you want to group a player(1) team(2) more options(3) or exit(4)")
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
            add = input("Do you want to add this player to a roster? Yes/No> ")
            name = first + ' ' + last
            if add == 'Yes' or add == 'yes':
                if team in roster:
                    stats_1 = player.Player_Profile()
                    get_stats = roster.get(team)
                    all_stats = stats_1 + ' ' + get_stats
                    roster[team] = all_stats
                    print("You added", name)
                    print(roster)
                    
                else:
                    stats = player.Player_Profile()
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
            add = input("Do you want to add this team to the list of teams? Yes/No> ")
            team1 = Team(team, location, wins, losses, ties)
            if add == 'yes' or add == 'Yes':
                record = team1.Record()
                teams[location] = record
                print(teams)
                
        
        
        elif choice == '3':
            printer = input("""
print a teams roster(1) print list of teams(2)
""")
            
            if printer == '1':
                print(roster)
            elif printer == '2':
                print(teams)
        
        
        
        
        elif choice == '4':
            print("Thank you, goodbye")
            go = False
        else:
            print("That's not an option")
      
      
#Main code_____________
      
main()
#1. one of the main diffrences between is the re use of the same code
#you can make a class that can do the same thing over and over instead of re writing the code over and over
#
#2. my code would have alot more functions that would do the things that the things the classes do 
#
#3. An addvantage of having OOP is the effciency of the code, it can cut the code length drastically
#
#4. a disadvantage of having OOP is the complicity of the code itself, some code in my case doesnt need very complex classes and OOP. 
#It can be very useful in some cases but somntimes it is easier just to do it the old fastion way 

        
        
