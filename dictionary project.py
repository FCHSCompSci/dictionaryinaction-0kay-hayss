hp_profile = {
    'display_name': 'life0fhayss',
    'house': 'gryfindor',
    'xp_in_game': 1000,
    'year_in_game': 1,
    }

while True:
    new_name = input("What is your new username? Press stop to quit: ")
    if new_name == "stop":
        break
    elif new_name != "":
        hp_profile['display_name'] = new_name
        break
while True:
    new_house = input("Do you want to be resorted? Press stop to quit")
    if new_house == "stop":
        break
    elif new_house != "":
        hp_profile['house'] = new_house
        break









    
    
    
    
    
    
