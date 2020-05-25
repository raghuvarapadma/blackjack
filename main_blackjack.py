# main_blackjack.py

# import statments
from functions.bets.bets import *
from functions.initializers.initializers import *
from functions.moves.moves import *
from functions.end_moves.end_moves import * 
from classes.classes import *

# main function
def main():
    # Welcome to the Game of Blackjack!
    print("Welcome to the game of Blackjack!")

    # Creating the players
    players_in_game = players_in_game_func()
    players = [None] * players_in_game
    dict_players = {}
    for i in range(players_in_game):
        assign_player(i, players, dict_players)
    dealer = Hand()

    # Creating chips for each player
    chips_of_players = [None] * players_in_game
    for i in range(players_in_game):
        assign_chips_player(i, chips_of_players, dict_players)

    # Creating deck and then shuffling
    deck_players = Deck()
    for i in range(0, 8):
        deck_new = Deck()
        deck_new.shuffle()
        deck_players.append(deck_new)
     
    # This statement below will display all cards in the deck, used for degugging    
    # print(str(deck_players))

    # This is where each round begins
    round_game = True
    while round_game:
        # Sub Arrays
        original = []
        surrender = []
        split_b = []
        before_chips = []
        blackjack_players = []
        insur_arr = []
        
        # Welcome Statment
        new_line()
        new_line()
        print("Welcome to a new round of Blackjack!")
        
        # Erasing player and dealer values
        for i in range(players_in_game):
            players[i].value = 0
            players[i].current_hand = []
        dealer.current_hand = []
        dealer.value = 0
        
        # Betting
        new_line()
        for i in range(players_in_game):
            bet = take_bet(i, dict_players)
            chips_of_players[i].bet = bet
            
        # Listing bets of each player
        new_line()
        for i in range(players_in_game):
            display_original_bet(i, chips_of_players, dict_players)
            
        # Dealing to all
        new_line()
        print("Dealing...")
        for i in range(0, players_in_game):
            first_card_player = deck_players.deal_card()
            players[i].add_card(first_card_player)
            if (first_card_player == "Ace"):
                print(dict_players[i] + "\'s first card was an ace!")
                print(dict_players[i] + "\'s current value is: " + str(players[i].value))
                players[i].aces_choice()
        
        first_card_dealer = deck_players.deal_card()
        if (first_card_dealer == "Ace"):
            dealer.value += 11
        second_card_dealer = deck_players.deal_card()
        dealer.add_card(first_card_dealer)
        
        for i in range(0, players_in_game):
            second_card_player = deck_players.deal_card()
            players[i].add_card(second_card_player)
            if (second_card_player == "Ace"):
                print(dict_players[i] + "\'s second card was an ace!")
                print(dict_players[i] + "\'s current value is: " + str(players[i].value))
                players[i].aces_choice()
        
        # Showing the cards to the player and the dealer
        new_line()
        for i in range(0, players_in_game):
            print(dict_players[i] + "\'s Cards: " + players[i].print_card(2))
            print(dict_players[i] + "\'s Value: " + str(players[i].value))
        print("Dealer Cards: " + dealer.print_card(1))
        print("Dealer's Value: " + str(dealer.value))
        
        # Player checking for blackjack
        real_play = True
        for i in range(0, players_in_game):
            if (players[i].value == 21):
                blackjack_players.append(i)
                print(dict_players[i] + " has a blackjack!")
                
        # Early Surrender Option
        for i in range(0, players_in_game):
            incorrect_blackjack = True
            for j in range(0, len(blackjack_players)):
                if blackjack_players[j] == i:
                    incorrect_blackjack = False
            surr_now = input(dict_players[i] + " do you want to surrender now? ")
            if (surr_now.lower() == "yes" and incorrect_blackjack):
                surrender.append(i)
            elif (surr_now.lower() == "yes" and not(incorrect_blackjack)):
                print(dict_players[i] + " already has a blackjack!")
            else:
                print(dict_players[i] + " does not want to surrender!")
        
        # Dealer checking for blackjack
        if (first_card_dealer == "Ace"):
            for i in range(0, players_in_game):
                if ((i in surrender)):
                    print("You have already surrendered!")
                else:
                    collect_insurance(players[i], dict_players, chips_of_players[i], i, insur_arr)
            if (second_card_dealer == "King" or second_card_dealer == "Queen" or second_card_dealer == "Jack" or second_card_dealer == "Ten"):
                real_play = False
                dealer.add_card(second_card_dealer)
                print("Dealer has blackjack!")
                print("Dealer Cards: " + dealer.print_card(2))
                print("Dealer's Value: " + str(dealer.value))
            else:
                real_play = True
                print("Dealer does not have blackjack!")
        elif (first_card_dealer == "King" or first_card_dealer == "Queen" or first_card_dealer == "Jack" or first_card_dealer == "Ten"):
            if (second_card_dealer == "Ace"):
                real_play = False
                dealer.add_card(second_card_dealer)
                dealer.value += 11
                print("Dealer has blackjack!")
                print("Dealer Cards: " + dealer.print_card(2))
                print("Dealer's Value: " + str(dealer.value))
            else:
                real_play = True
                print("Dealer does not have blackjack!")
        else:
            real_play = True
            print("Dealer does not have blackjack!")

        # Logic based on if dealer has blackjack or not
        if real_play == False:
            normal = []
            for i in range(0, players_in_game):
                surr = False
                for j in range(0, len(surrender)):
                    if surrender[j] == i:
                        surr = True
                if surr == False:
                    normal.append(i)
                    
            for j in range(0, len(surrender)):
                surrender_opt(chips_of_players[surrender[j]], surrender[j], dict_players)
            for l in range(0, len(normal)):
                if (players[normal[l]].value < 21):
                    player_loses(players[normal[l]], chips_of_players[normal[l]], normal[l], dict_players)
                    original.append(l)
                    if (normal[l] in insur_arr):
                        insurance_normal(chips_of_players[l], l, dict_players)
                elif (players[normal[l]].value == 21):
                    if (normal[l] in insur_arr):
                        insurance_blackjack(chips_of_players[l], l, dict_players)
                    else:
                        push(players[normal[l]], normal[l], dict_players)
        else: 
            # Player's turn to play the round
            new_line()
            while real_play:
                playing = True
                while playing:
                    for i in range(0, players_in_game):
                        blackjack = False
                        for j in range(0, len(blackjack_players)):
                            if blackjack_players[j] == i:
                                blackjack = True
                        surr_play = False
                        for j in range(0, len(surrender)):
                            if surrender[j] == i:
                                surr_play = True
                        if (blackjack == True):
                            print(dict_players[i] + " you already have a blackjack!")
                        elif (surr_play == True):
                            print(dict_players[i] + " you have already surrendered!")
                        else:
                            j = 2
                            print(dict_players[i] + "\'s Cards: " + players[i].print_card(j))
                            print(dict_players[i] + "\'s Value: " + str(players[i].value))
                            play = choose(i, dict_players, players[i])
                            start_turn = True
                            while start_turn:
                                if (play == "hit"):
                                    original.append(i)
                                    hit(deck_players, players[i])
                                    j += 1
                                    print(dict_players[i] + "\'s Cards: " + players[i].print_card(j))
                                    print(dict_players[i] + "\'s Value: " + str(players[i].value))
                                    continue_play = True
                                    while continue_play:
                                        if (players[i].value > 21):
                                            print("You busted.")
                                            break
                                        h_o_s = hit_or_stand(deck_players, players[i], i, dict_players)
                                        if (h_o_s == True):
                                            j +=1
                                            print(dict_players[i] + "\'s Cards: " + players[i].print_card(j))
                                            print(dict_players[i] + "\'s Value: " + str(players[i].value))
                                        else:
                                            break
                                    break
                                elif (play == "stand"):
                                    original.append(i)
                                    break
                                elif (play == "surrender"):
                                    surrender.append(i)
                                    break
                                elif (play == "double down"):
                                    double_down(deck_players, players[i], chips_of_players[i], i, dict_players)
                                    original.append(i)
                                    break
                                elif (play == "split"):
                                    before_chips.append(chips_of_players[i].value - 100)
                                    a, b = split_blackjack(deck_players, players[i], chips_of_players[i], i, dict_players)
                                    players[i] = a
                                    chips_of_players[i] = b
                                    split_b.append(i)
                                    break
                    break

                # Dealer's turn to flip
                new_line()
                dealer.add_card(second_card_dealer)
                if (second_card_dealer == "Ace"):
                    if (first_card_dealer == "Ace"):
                        dealer.value += 1
                    else:
                        dealer.value += 11
                #check for ace
                print("Dealer flipped the second card! Dealer's Cards: " + dealer.print_card(2))
                print("Dealer Value: " + str(dealer.value))

                # Dealer Below 17
                new_line()
                a = 2
                while dealer.value < 17:
                    print("Dealer is under 17!")
                    a += 1
                    extra_card = deck_players.deal_card()
                    dealer.add_card(extra_card)
                    if (extra_card == "Ace"):
                        if (dealer.value < 11):
                            dealer.value += 11
                        else:
                            dealer.value += 1
                    print("Dealer was under 17 and drew card! Dealer Cards: " + dealer.print_card(a))
                    print("Dealer Value: " + str(dealer.value))

                # Show all cards and values
                for i in range(0, len(blackjack_players)):
                    print(dict_players[blackjack_players[i]] + "\'s Cards: " + players[blackjack_players[i]].print_card(len(players[blackjack_players[i]].current_hand)))
                    print(dict_players[blackjack_players[i]] + "\'s value: " + str(players[blackjack_players[i]].value))
                for i in range(0, len(original)):
                    print(dict_players[original[i]] + "\'s Cards: " + players[original[i]].print_card(len(players[original[i]].current_hand)))
                    print(dict_players[original[i]] + "\'s value: " + str(players[original[i]].value))
                for i in range(0, len(surrender)):
                    print(dict_players[surrender[i]] + "\'s Cards: " + players[surrender[i]].print_card(len(players[surrender[i]].current_hand)))
                    print(dict_players[surrender[i]] + "\'s value: " + str(players[surrender[i]].value))
                for i in range(0, len(split_b)):
                    for j in range(0, len(players[split_b[i]])):
                        print(dict_players[split_b[i]] + "\'s Cards: " + players[split_b[i]][j].print_card(len(players[split_b[i]][j].current_hand)))
                        print(dict_players[split_b[i]] + "\'s value: " + str(players[split_b[i]][j].value))
                print("Dealer Cards: " + dealer.print_card(a))
                print("Dealer Value: " + str(dealer.value))


                # Winning and Losing Rounds
                new_line()
                if (dealer.value > 21):
                    dealer_busts(dealer)
                # Insurance
                for i in range(0, len(insur_arr)):
                    insurance_lost(chips_of_players[insur_arr[i]], insur_arr[i], dict_players)
                # Blackjack
                for i in range(0, len(blackjack_players)):
                    player_wins_21(players[blackjack_players[i]], chips_of_players[blackjack_players[i]], blackjack_players[i], dict_players)
                # hit, stand, double down (original)
                for i in range(0, len(original)):
                    if (dealer.value > 21):
                        if (players[original[i]].value > 21):
                            player_busts(players[original[i]], chips_of_players[original[i]], original[i], dict_players)
                        else:
                            player_wins(players[original[i]], chips_of_players[original[i]], original[i], dict_players)
                    else:
                        if (players[original[i]].value > 21):
                            player_busts(players[i], chips_of_players[original[i]], original[i], dict_players)
                        else:
                            if (players[original[i]].value > dealer.value):
                                player_wins(players[i], chips_of_players[original[i]], original[i], dict_players)
                            elif (players[original[i]].value < dealer.value):
                                player_loses(players[i], chips_of_players[original[i]], original[i], dict_players)
                            else:
                                push(players[original[i]], original[i], dict_players)
                # surrender
                for i in range(0, len(surrender)):
                    surrender_opt(chips_of_players[surrender[i]], surrender[i], dict_players)
                # split   
                for i in range(0, len(split_b)):
                    for j in range (0, len(players[split_b[i]])):
                        if (dealer.value > 21):
                            if (players[split_b[i]][j] > 21):
                                player_busts_split(chips_of_players[split_b[i]][j], split_b[i], j, dict_players)
                            else:
                                player_won_split(chips_of_players[split_b[i]][j], split_b[i], j, dict_players)
                        else:
                            if (players[split_b[i]][j].value > 21):
                                player_busts_split(chips_of_players[split_b[i]][j], [split_b[i]], j, dict_players)
                            else:
                                if (players[split_b[i]][j].value > dealer.value):
                                    player_won_split(chips_of_players[split_b[i]][j], split_b[i], j, dict_players)
                                elif (players[split_b[i]][j].value < dealer.value):
                                    player_loses_split(chips_of_players[split_b[i]][j], split_b[i], j, dict_players)
                                else:
                                    player_push_split(chips_of_players[split_b[i]][j], split_b[i], j, dict_players)
                break

        # Play Again
        new_line()
        while True:
            try:
                ask = input("Do you want to play another round? ")
            except:
                print("Please enter a vlid response!")
                continue
            else:
                if (ask.lower() == "yes"):
                    round_game = True
                    for i in range(0, len(split_b)):
                        val_chip = 0
                        for j in range(0, len(players[split_b[i]])):
                            val_chip += (chips_of_players[split_b[i]][j].value - 100)
                        players[split_b[i]] = Hand()
                        chips_of_players[split_b[i]] = Chips()
                        chips_of_players[split_b[i]].value = val_chip + 100 + before_chips[split_b[i]]
                    for i in range(0, len(blackjack_players)):
                        print(dict_players[blackjack_players[i]] + "\'s chips: " + str(chips_of_players[blackjack_players[i]].value))
                    for i in range(0, len(original)):
                        print(dict_players[original[i]] + "\'s chips: " + str(chips_of_players[original[i]].value))
                    for i in range(0, len(surrender)):
                        print(dict_players[surrender[i]] + "\'s chips: " + str(chips_of_players[surrender[i]].value))
                    for i in range(0, len(split_b)):
                        print(dict_players[split_b[i]] + "\'s chips: " + str(chips_of_players[split_b[i]].value))
                elif (ask.lower() == "no"):
                    round_game = False
                    for i in range(0, len(split_b)):
                        val_chip = 0
                        for j in range(0, len(players[split_b[i]])):
                            val_chip += (chips_of_players[split_b[i]][j].value - 100)
                        players[split_b[i]] = Hand()
                        chips_of_players[split_b[i]] = Chips()
                        chips_of_players[split_b[i]].value = val_chip + 100 + before_chips[split_b[i]]
                    for i in range(0, len(blackjack_players)):
                        print(dict_players[blackjack_players[i]] + " ended with " + str(chips_of_players[blackjack_players[i]].value) + " chips!")
                    for i in range(0, len(original)):
                        print(dict_players[original[i]] + " ended with " + str(chips_of_players[original[i]].value) + " chips!")
                    for i in range(0, len(surrender)):
                        print(dict_players[surrender[i]] + " ended with " + str(chips_of_players[surrender[i]].value) + " chips!")
                    for i in range(0, len(split_b)):
                        print(dict_players[split_b[i]] + " ended with " + str(chips_of_players[split_b[i]].value) + " chips!")
                break
            break

if __name__ == '__main__':
    main()
