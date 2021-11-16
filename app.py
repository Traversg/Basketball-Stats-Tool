import constants
import copy

if __name__ == "__main__":
    players = copy.deepcopy(constants.PLAYERS)
    teams = copy.deepcopy(constants.TEAMS)
    panthers = []
    bandits = []
    warriors = []
    experienced_player = []
    inexperienced_player = []
    num_players_team = int(len(players) / len(teams))
    
    def clean_data():
        for player in players:
            player['guardians'] = player['guardians'].split(' and ')
            player['height'] = int(player['height'][:2])
            if player['experience'] == 'YES':
                player['experience'] = True
            else: 
                player['experience'] = False
                
    
    def balance_team(*teams):
        def balance_experience(experience):
            for i in range(0, int((num_players_team / 2))):
                team.append(experience[0])
                experience.pop(0)
        
        for player in players:
            if player['experience'] == True:
                experienced_player.append(player)
            elif player['experience'] == False:
                inexperienced_player.append(player)
                
        for team in teams:
            balance_experience(experienced_player)
            balance_experience(inexperienced_player)
    
    
    def team_stats(team_name, team):
        team_names = []
        experienced = []
        inexperienced = []
        player_height = []
        guardians = []
        guardian_list = []
        
        for person in team:
            team_names.append(person['name'])
            if person['experience'] == True:
                experienced.append(person)
            elif person['experience'] == False:
                inexperienced.append(person)
            player_height.append(person['height'])
            guardians.append(person['guardians'])
        
        
        print(f'''\nTeam: {team_name} Stats
{('-' * 20)}
Total players: {int(len(team))}
Total experienced: {int(len(experienced))}
Total inexperienced: {int(len(inexperienced))}
Average height: {int((sum(player_height) / num_players_team))}\n
Players on Team:
{', '.join(team_names)}
\nGuardians:''')
        
        for i, guardian in enumerate(guardians):
            guardian_list += guardians[i]
        
        print(', '.join(guardian_list))
        
    
    clean_data()
    
    balance_team(panthers, bandits, warriors)
    
    while True:
        print(f'''\nBASKETBALL TEAM STATS TOOL\n
{('-' * 4) + ' MENU ' + ('-' * 4)}\n
Here are your choices:\nA) Display Team Stats\nB) Quit\n''')
        
        display_or_quit = input('Enter an option: ')
        
        if display_or_quit.upper() == 'A':
            print('\nA) Panthers\nB) Bandits\nC) Warriors\n')
        elif display_or_quit.upper() == 'B':
            print('Goodbye!')
            break
            
        team_choice = input('Enter an option: ')
        
        if team_choice.upper() == 'A':
            team_stats('Panthers', panthers)
        if team_choice.upper() == 'B':
            team_stats('Bandits', bandits)
        if team_choice.upper() == 'C':
            team_stats('Warriors', warriors)
        
            
                  
