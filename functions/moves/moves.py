# moves.py

# imports the Hand and Chips class
from classes.classes import Hand, Chips

def hit(deck, hand):
    card = deck.deal_card()
    print("You got a " + card + "!")
    hand.add_card(card)
    if (card == "Ace"):
        hand.aces_choice()
        
def hit_or_stand(deck, hand, i, dict_ref):
    while True:
        try:
            response = input("Hit or Stand? ")
        except:
            print("Enter a valid response!")
            continue
        else:
            if response.lower() == "hit":
                hit(deck, hand)
                print(dict_ref[i] + " decided to hit")
                return True
            elif response.lower() == "stand":
                print(dict_ref[i] + " decided to stand")
                return False
            else:
                continue

def double_down(deck, hand, chips, i, dict_ref):
    card = deck.deal_card()
    print("You got a " + card + "!")
    hand.add_card(card)
    if (card == "Ace"):
        hand.aces_choice()
    chips.bet *= 2
    print(dict_ref[i] + " you're turn is finished!")
    
def split_blackjack(deck, hand, chips, i, dict_ref):
    chips1 = Chips()
    chips2 = Chips()
    new_chips = []
    new_chips.append(chips1)
    new_chips.append(chips2)
    new_chips[0].bet = chips.bet
    new_chips[1].bet = chips.bet
    hand1 = Hand()
    hand2 = Hand()
    newHand = []
    newHand.append(hand1)
    newHand.append(hand2)
    newHand[0].add_card(hand.current_hand[0])
    newHand[1].add_card(hand.current_hand[1])
    if (hand.current_hand[0] == "Ace" and hand.current_hand[1] == "Ace"):
        print("Since you have two aces, you will be dealed one card per hand!")
        card_one = deck.deal_card()
        card_two = deck.deal_card()
        newHand[0].add_card(card_one)
        newHand[1].add_card(card_two)
        print(dict_players[i] + "\'s Cards for their first hand: " + newHand[0].print_card(2))
        print(dict_players[i] + "\'s Value for their first hand: " + str(newHand[0].value))    
        print(dict_players[i] + "\'s Cards for their second hand: " + newHand[1].print_card(2))
        print(dict_players[i] + "\'s Value for their second hand: " + str(newHand[1].value))       
    else:
        card_one = deck.deal_card()
        newHand[0].add_card(card_one)
        one = 2
        print(dict_players[i] + "\'s Cards for their first hand: " + newHand[0].print_card(one))
        print(dict_players[i] + "\'s Value for their first hand: " + str(newHand[0].value))
        play_one = True
        while play_one:
            try:
                response_split_one = input("Do you want to hit, stand, or double down?")
            except:
                print("Please enter a valid response!")
                continue
            else:
                if (response_split_one.lower() == "hit"):
                    ("You chose to hit!")
                    hit(deck, newHand[0])
                    one += 1
                    print(dict_players[i] + "\'s Cards for their first hand: " + newHand[0].print_card(one))
                    print(dict_players[i] + "\'s Value for their first hand: " + str(newHand[0].value))
                    play_one = True
                    while play_one:
                        if (newHand[0].value > 21):
                            print("You busted.")
                            break
                        h_o_s = hit_or_stand(deck_players, newHand[0], i, dict_players)
                        if (h_o_s == True):
                            one +=1
                            print(dict_players[i] + "\'s Cards for their first hand: " + newHand[0].print_card(one))
                            print(dict_players[i] + "\'s Value for their first hand: " + str(newHand[0].value))
                        else:
                            break
                    break
                elif (response_split_one.lower() == "stand"):
                    print("You chose to stand!")
                    break
                elif (response_split_one.lower() == "double down"):
                    print("You chose to double down!")
                    double_down(deck, newHand[0], new_chips[0], i, dict_ref)
                    break
                    
        card_two = deck.deal_card()
        newHand[1].add_card(card_two)
        two = 2
        print(dict_players[i] + "\'s Cards for their second hand: " + newHand[1].print_card(two))
        print(dict_players[i] + "\'s Value for their second hand: " + str(newHand[1].value))
        play_two = True
        while play_two:
            try:
                response_split_two = input("Do you want to hit, stand, or double down?")
            except:
                print("Please enter a valid response!")
                continue
            else:
                if (response_split_two.lower() == "hit"):
                    ("You chose to hit!")
                    hit(deck, newHand[1])
                    two += 1
                    print(dict_players[i] + "\'s Cards for their second hand: " + newHand[1].print_card(two))
                    print(dict_players[i] + "\'s Value for their second hand: " + str(newHand[1].value))
                    play_two = True
                    while play_two:
                        if (newHand[1].value > 21):
                            print("You busted.")
                            break
                        h_o_s = hit_or_stand(deck_players, newHand[1], i, dict_players)
                        if (h_o_s == True):
                            two +=1
                            print(dict_players[i] + "\'s Cards for their second hand: " + newHand[1].print_card(two))
                            print(dict_players[i] + "\'s Value for their second hand: " + str(newHand[1].value))
                        else:
                            break
                    break
                elif (response_split_two.lower() == "stand"):
                    print("You chose to stand!")
                    break
                elif (response_split_two.lower() == "double down"):
                    print("You chose to double down!")
                    double_down(deck, newHand[1], new_chips[1], i, dict_ref)
                    break
    return newHand, new_chips

def choose(i, dict_ref, hand):
    while True:
        try:
            response = input("Would you like to hit, stand, surrender, split, or double down? ")
        except:
            print("Please enter a valid response!")
            continue
        else:
            if (response.lower() == "hit"):
                print(dict_ref[i] + " chose to hit!")
                return "hit"
                break
            elif (response.lower() == "stand"):
                print(dict_ref[i] + " decided to stand!")
                return "stand"
                break
            elif (response.lower() == "surrender"):
                print(dict_ref[i] + " chose to surrender!")
                return "surrender"
                break
            elif (response.lower() == "split"):
                if (hand.current_hand[0] == hand.current_hand[1]):
                    print(dict_ref[i] + " chose to split!")
                    return "split"
                    break
                else:
                    print("You can only split if you have two of the same kind!")
                    continue
            elif (response.lower() == "double down"):
                print(dict_ref[i] + " chose to double down")
                return "double down"
                break
            else:
                print("Please enter a valid repsonse!")
                continue
                
def collect_insurance(player, dict_ref, chips, i, insur_array):
    if player.value == 21:
        try:
            blackjack_response = input(dict_ref[i] + " would you like insurance? ")
        except TypeError:
            print("Please provide a valid answer!")
        else:
            if (blackjack_response.lower() == "yes"):
                insur_array.append(i)
                chips.insurance = (chips.bet/2)
                print(dict_ref[i] + " made a bet of " + str(chips.insurance) + " for insurance!")
            else:
                print(dict_ref[i] + " you do not want insurance!")
    else:
        try:
            normal_response = input(dict_ref[i] + " would you like insurance? ")
        except TypeError:
            print("Please provide a valid answer!")
        else:
            if (normal_response.lower() == "yes"):
                insur_array.append(i)
                chips.insurance = chips.bet/2
                print(dict_ref[i] + " made a bet of " + str(chips.insurance) + " for insurance!")
            else:
                print(dict_ref[i] + " you do not want insurance!")