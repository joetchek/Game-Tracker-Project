class Game_Component:

    #init for Game_Component class
    #Variable Definitions
    #name --- name of game - pulled from igdb but can be manually set by user
    #rating --- rating of game given by user
    #date_released --- release date of the game 
    #date_complete --- date user inputs as game complete
    #hours --- hours user logs in game
    def __init__(self, name: str, rating: int, date_released: str, date_complete: str, hours: float) -> None:
        self.name = name
        self.rating = rating
        self.date_released = date_released
        self.date_complete = date_complete
        self.hours = hours

    #changes name
    def set_name(self, new_name):
        self.name = new_name

    #changes rating
    def set_rating(self, new_rating):
        self.rating = new_rating

    #changes hours
    def set_hours(self, new_hours):
        self.hours = new_hours

    #changes date complete
    def set_date_complete(self, new_date):
        self.date_complete = new_date

    #changes date released
    def set_date_released(self, new_date):
        self.date_released = new_date

    def __str__(self) -> str:
        return f'Name: {self.name}\nRating: {self.rating}\nHours: {self.hours}\nDate Released: {self.date_released}\nDate Complete: {self.date_complete}'

    def return_as_dict(self) -> dict:
        return_dict = {}
        return_dict['name'] = self.name
        return_dict['rating'] = self.rating
        return_dict['hours'] = self.hours
        return_dict['date_released'] = self.date_released
        return_dict['date_completed'] = self.date_complete

        return return_dict