import access_varibles as av
from igdb.wrapper import IGDBWrapper
import json

wrapper = IGDBWrapper(av.client_id, av.access_token)

# result = wrapper.api_request('games', 'fields id, name; search \"Zelda\";')
# answer = json.loads(result)
# print(answer)

name = input('Enter search term: ')

#test query of the game api
result = wrapper.api_request('games', f'fields name, rating; where name ~ *\"{name}\"*; limit 50; sort rating desc;')
# print(result)
answer = json.loads(result)
print(answer)

#writes to json file called test
with open("test.json", "w") as output:
    json.dump(answer, output)