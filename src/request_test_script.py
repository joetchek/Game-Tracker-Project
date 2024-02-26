from igdb.wrapper import IGDBWrapper
import json
import os
from game_manager import Game_Manager

# client_id = os.environ.get('ClientID')
# access_token = os.environ.get('AccessToken')
# print(client_id)
# print(access_token)
# wrapper = IGDBWrapper(client_id, access_token)

# result = wrapper.api_request('games', 'fields id, name; search \"Zelda\";')
# answer = json.loads(result)
# print(answer)

# name = input('Enter search term: ')

# #test query of the game api
# result = wrapper.api_request('games', f'fields name, rating; where name ~ *\"{name}\"*; limit 50; sort rating desc;')
# # print(result)
# answer = json.loads(result)
# #print(answer)

# #writes to json file called test
# with open("test.json", "w") as output:
#     json.dump(answer, output)

manager = Game_Manager()
# test_search = manager.igdb_search()
# ans = manager.select_by_name(test_search)
# print(ans)
# print(test_search[ans])
manager.user_prompt()