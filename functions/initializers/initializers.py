# initializers.py

# imports the Hand and Chips class
from classes.classes import Hand, Chips

def players_in_game_func():
    while True:
        try: 
            players_in_game_response = int(input("How many players are playing? "))
        except:
            print("Please enter an integer!")
            continue
        else:
            print(str(players_in_game_response) + " are playing! Let's get ready to play!")
            return players_in_game_response
            break

def assign_player(i, hand, dict_ref):
    hand[i] = Hand()
    name = input("What is your name? ")
    dict_ref[i] = name            
            
def assign_chips_player(i, chips, dict_ref):
    chips[i] = Chips()
    print(dict_ref[i] + " has " + str(chips[i].value) + " chips!")

def new_line():
    print("\n")