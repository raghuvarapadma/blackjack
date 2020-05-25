# bets.py

# This functions takes the bet of the player
def take_bet(i, dict_ref):
    while True:
        try:
            bet = int(input(dict_ref[i] + " how much do you want to bet? "))
        except:
            print("Please enter an integer")
            continue
        else:
            break
    return bet

# This function displays the original bet of the player
def display_original_bet(i, chips, dict_ref):
    print(dict_ref[i] + " bets " + str(chips[i].bet))