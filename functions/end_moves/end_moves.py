# end_moves.py

# imports the Chips class
from classes.classes import Chips

def player_wins_21(player, chips, i, dict_ref):
    print(dict_ref[i] + " wins by blackjack!")
    chips.won_bet_blackjack()

def player_wins(player, chips, i, dict_ref):
    print(dict_ref[i] + " wins!")
    chips.won_bet()

def player_loses(player, chips, i, dict_ref):
    print(dict_ref[i] + " loses!")
    chips.lost_bet()

def player_busts(player, chips, i, dict_ref):
    print(dict_ref[i] + " busts!")
    chips.lost_bet()
    
def push(player, i, dict_ref):
    print("Tie! " + dict_ref[i] + " draws with the dealer!")
    
def dealer_busts(dealer):
    print("Dealer busts! Value is " + str(dealer.value) + "!")
    
def player_busts_split(chips, i, j, dict_ref):
    print("Hand " + str(j) + " belonging to " + dict_ref[i] + " busts!")
    chips.bust_split()

def player_won_split(chips, i, j, dict_ref):
    print("Hand " + str(j) + " belonging to " + dict_ref[i] + " wins!")
    chips.won_split()
    
def player_loses_split(chips, i, j, dict_ref):
    print("Hand " + str(j) + " belonging to " + dict_ref[i] + " loses!")
    chips.lost_split()
    
def player_push_split(chips, i, j, dict_ref):
    print("Hand " + str(j) + " belonging to " + dict_ref[i] + " ties with dealer!")
    
def surrender_opt(chips, i, dict_ref):
    print(dict_ref[i] + " chose to surrender!")
    chips.lost_surrender()
    
def insurance_normal(chips, i, dict_ref):
    print(dict_ref[i] + " chose to have insurance!")
    chips.insurance_money_won()

def insurance_blackjack(chips, i, dict_ref):
    print(dict_ref[i] + " has insurance and was paid already!")
    chips.insurance_money_won()

def insurance_lost(chips, i, dict_ref):
    print("You bet on insurance and lost money!")
    chips.insurance_money_loss()