from json_parser import JSON_Parser
from game_component import Game_Component
import os
import json
from igdb.wrapper import IGDBWrapper
import datetime

#TODO -- function that calls the IGDB and returns 25 search results - DONE
#TODO -- function that reads in a JSON file and makes game components for all of the files - DONE
#TODO -- move the add to file function to this class - DONE
#TODO -- function that asks user for input and makes new game component

parser = JSON_Parser()
client_id = os.environ.get('ClientID')
access_token = os.environ.get('AccessToken')
wrapper = IGDBWrapper(client_id, access_token)

class Game_Manager:
    #initializes game list, game_list is a list of game components
    def __init__(self) -> None:
        self.game_list = []

    #takes in dict and returns game component with dict keywords
    def json_to_game(self, json_data: dict) -> Game_Component:

        name = 'N/A'
        platform = 'N/A'
        r_date = 'N/A'
        c_date = 'N/A'
        rating = 0
        hours = 0
        
        if 'name' in json_data:
            name = json_data['name']
        elif 'rating' in json_data:
            rating = json_data['rating']
        elif 'date_released' in json_data:
            r_date = json_data['date_released']
        elif 'date_completed' in json_data:
            c_date = json_data['date_completed']
        elif 'platfrom' in json_data:
            platform = json_data['platform']
        elif 'hours' in json_data:
            hours = json_data['hours']

        game = Game_Component(name, rating, r_date, c_date, hours, platform)
        return game
            
        
    #reads in a set file with the saved games in json format, file will be static as it will be created
    #and appended by this program
    def read_saved_games(self):
        data = parser.read_file('games.json') #read the data in
        for game in data: #make sure all the keys are there
            component = self.json_to_game(game)
            self.game_list.append(component)

    #turns game component into a dict and adds it to the json file
    def add_games_to_file(self):
        write_list = [] #create a temporary write list 
        for game in self.game_list:
            game_data = game.return_as_dict()
            parser.add_to_file(write_list, game_data, 'games.json')

    #adds a new game compenent to the list
    def add_game_component(self, component: Game_Component):
        self.game_list.append(component)

    #prints out the list of games
    def print_game_list(self):
        for game in self.game_list:
            print(game)

    #searches top 25 games by search term
    def igdb_search(self) -> list:
        name = input('Enter search term: ')
        result = wrapper.api_request('games', f'fields name, rating, first_release_date; where name ~ *\"{name}\"*; limit 25; sort rating desc;')
        answer = json.loads(result)
        return answer
    
    #prompts user to select game name by number
    def select_by_name(self, json_data: list) -> int:
        i = 0
        for game in json_data:
            print(f'{i+1}: {game['name']}')
            i += 1

        #logic loop to verify user input
        answer = len(json_data) + 1
        while (answer > len(json_data)):
            answer = int(input('Select number of game to add: '))
            if answer > len(json_data):
                print('Try again')

        return answer - 1
    
    #prompts user for search term and creates game component
    def user_prompt(self):
        json_data = {} #initializes data
        selection_list = self.igdb_search() #searches the database
        answer = self.select_by_name(selection_list) #prompts user for select

        json_data = selection_list[answer] #grabs 
        r_date = json_data['first_release_date']
        r_date_formatted = datetime.date.fromtimestamp(r_date) #formates database date
        date_string = "{:%B %d, %Y}".format(r_date_formatted)
        print(json_data)
        del json_data['id'] #deletes unneeded id key
        del json_data['first_release_date'] #deletes unneeded date key
        json_data['date_released'] = date_string # sets new key to formatted date
        print(json_data)
        #WORKING FOR NOW, TMMRW NEED TO ADD INPUT FOR OTHER KEYS AND WRITE TO FILE


        



# manager = Game_Manager()
# manager.read_saved_games()
# manager.print_game_list()
# comp = Game_Component('n', 99, '1', '1', 22)   
# manager.add_game_component(comp)   
# manager.print_game_list()
# manager.add_games_to_file()
    