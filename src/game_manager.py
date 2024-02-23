from json_parser import JSON_Parser
from game_component import Game_Component
import os
import json
from igdb.wrapper import IGDBWrapper

#TODO -- function that calls the IGDB and returns 25 search results
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
        
    #reads in a set file with the saved games in json format, file will be static as it will be created
    #and appended by this program
    def read_saved_games(self):
        data = parser.read_file('games.json') #read the data in
        for game in data: #make sure all the keys are there
            if not 'name' in game.keys():
                game['name'] = 'N/A'
            elif not 'rating' in game.keys():
                game['rating'] = 0
            elif not 'hours' in game.keys():
                game['hours'] = 0.0
            elif not 'date_released' in game.keys():
                game['date_released'] = 'N/A'
            elif not 'date_completed' in game.keys():
                game['date_completed'] = 'N/A'
            
            #create the component
            component = Game_Component(game['name'], game['rating'], game['date_released'], game['date_completed'], game['hours'])
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


#manager = Game_Manager()
# manager.read_saved_games()
# manager.print_game_list()
# comp = Game_Component('n', 99, '1', '1', 22)   
# manager.add_game_component(comp)   
# manager.print_game_list()
# manager.add_games_to_file()
    