import access_varibles as av
from igdb.wrapper import IGDBWrapper
import json

wrapper = IGDBWrapper(av.client_id, av.access_token)

# result = wrapper.api_request('games', 'fields id, name; search \"Zelda\";')
# answer = json.loads(result)
# print(answer)

name = input('Enter search term: ')

result = wrapper.api_request('games', f'fields name, rating; search \"{name}\";')
answer = json.loads(result)
print(answer)

