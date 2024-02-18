import json

#reads json file and returns list of dictionaries
def read_file(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        #print(data)
        return data
        
data_test = read_file('test.json') 

#TODO - create function for parsing through list and return a list with specified key values
#TODO - create function for printing JSON in readable format

# name_list = []
# id_list = []
# rating_list = []
# for i in data_test:
#     id_list.append(i['id'])
#     name_list.append(i['name'])
#     rating_list.append(i['rating'])

# print(name_list)

