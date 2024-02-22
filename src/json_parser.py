import json

#class for parsing json
class JSON_Parser:
    def __init__(self) -> None:
        pass

#reads json file and returns list of dictionaries
#json file is a json file in prohject directory
    def read_file(self, json_file: str) -> list:
        with open(json_file, 'r') as file:
            data = json.load(file)
            #print(data)
            return data

    #search through json data and return the values of a specified key
    #json_data is a list and key is a string
    def key_search(self, json_data: list, key: str) -> list:
        ret_list = [] #list of values at specified keys

        for i in json_data:
            if key in i.keys():
                print('Key found!') #if the key is in the dictionary
                ret_list.append(i[key]) #add the value to the list
            else:
                print('Key not found!')

        print(ret_list)
        return ret_list

    #reads in json list and prints the specified key in an ordered list
    #json_data is a list and key is a string
    def ordered_print(self, json_data: list, key: str):
        value_list = self.key_search(json_data, key)

        for i in range(len(value_list)):
            data = value_list[i]
            print(f'{i+1}: {data}')

    #gets json data and new dictionary to append and writes it to the file
    def add_to_file(self, data: list, new_data: dict, json_file: str) -> None:
        data.append(new_data)

        with open(json_file, 'w') as file:
            json.dump(data, file)


# test_class = JSON_Parser()
# test_data = test_class.read_file('test.json')
# test_class.ordered_print(test_data, 'name')

# test_add = {'id': 1111, 'name': 'test data', 'rating': 99.999}
# test_class.add_to_file(test_data, test_add, 'test.json')
# test_class.ordered_print(test_data, 'name')
