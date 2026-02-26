from game_functions import*
from random import randrange

def start_b():
    def get_card(pre_value, ace_count):
        nonlocal card_list
        new_card=False
        while not new_card:
            card=randrange(13)
            suit=randrange(4)
            deck_position=card+13*suit
            if card_list[deck_position]=="":
                card_list[deck_position]="x"
                new_card=True
        value=10
        if card==0:
            card_name="Ace"
            value=0
            ace_count+=1
        elif card==10:
            card_name="Jack"
        elif card==11:
            card_name="Queen"
        elif card==12:
            card_name="King"
        else:
            card_name=str(card+1)
            value=card+1
        if suit==0:
            suit_name=" of Hearts"
        elif suit==1:
            suit_name=" of Diamonds"
        elif suit==2:
            suit_name=" of Clubs"
        else:
            suit_name=" of Spades"
        value+=pre_value
        return card_name+suit_name, value, ace_count
    
    def ace_value(hand_value, ace_amount):
        new_value=hand_value
        total_ace_value=0
        for i in range(ace_amount):
            if new_value+11>21:
                total_ace_value+=1
                new_value+=1
            else:
                total_ace_value+=11
                new_value+=11
        return total_ace_value
    
    def value_actual(p_d="d"):
        nonlocal player_hand, player_aces
        nonlocal dealer_hand, dealer_aces
        if p_d=="p":
            return player_hand+ace_value(player_hand, player_aces)
        else:
            return dealer_hand+ace_value(dealer_hand, dealer_aces)
    
    def delete(message, file_overwrite):
        nonlocal inp
        while inp!="y" and inp!="n":
            inp = input(f"{message}?\nType \"y\" for yes or \"n\" for no\n").lower()
            match inp:
                case "y":
                    nonlocal balance; balance=100.0
                    if file_overwrite:
                        with open("balance.txt", "w") as save_del:
                            save_del.write(str(balance))
                    clear()
                    print("Save data deleted. Balance reset to $100")
                case "n":
                    clear()
                case _:
                    print("Invalid input, please type \"y\" or \"n\"")
    
    balance=100.0
    inp=None
    clear()
    try:
        with open("balance.txt") as save:
            balance=float(save.read())
        with open("balance.txt", "w") as save:
            save.write(str(balance))
    except FileNotFoundError:
        print("No save data. Creating save\n")
        try:
            with open("balance.txt", "w") as save:
                save.write(str(balance))
        except OSError:
            file_perm=False
        else:
            file_perm=True
    except ValueError:
        print("Save was corrupted\n")
        try:
            with open("balance.txt", "w") as save:
                save.write(str(balance))
        except OSError:
            file_perm=False
        else:
            file_perm=True
    except OSError:
        file_perm=False
    else:
        file_perm=True
    
    
    
    
    if not file_perm:
        print("Unable to access or create save data. Game will only be saved locally\n")
    print("""Hello, and welcome to blackjack. Start by joining a table:
---
Type "play" to join the table
Type "balance" to view current money amount
Type "help" for an explanation of how blackjack works
Type "delete save" to delete saved data from your computer
Type "quit" to quit
---""")
    while True:
        inp=input().lower()
        load(1)
        match inp:
            case "play":
                bet=100
                if balance>=.01:
                    bet_entered=False
                    while not bet_entered:
                        try:
                            inp = round(float(input("Enter bet amount:\n")), 2)
                        except ValueError:
                            print("Invalid input, please type a number")
                        else:
                            if inp>balance:
                                print(f"Bet cannot exceed current money amount\nCurrent balance: ${balance:.2f}")
                            elif inp<.01:
                                print("Bet cannot be negative or less than 1 cent")
                            else:
                                bet=inp
                                bet_entered=True
                    clear()
                else:
                    print("No money to bet. Bet automatically set to $100")
                balance-=bet
                card_list=[""]*52
                dealer_card_1, dealer_hand, dealer_aces=get_card(0, 0)
                dealer_card_2, dealer_hand, dealer_aces=get_card(dealer_hand, dealer_aces)
                player_card_1, player_hand, player_aces=get_card(0, 0)
                player_card_2, player_hand, player_aces=get_card(player_hand, player_aces)
                print("Dealer stands on 17\n---")
                print(f"Dealer's hand: {dealer_card_1}\n")
                print(f"Your hand: {player_card_1}, {player_card_2}")
                print(f"Value: {value_actual("p")}")
                print()
                _21=False
                next_card=None
                if value_actual("p")==21:
                    _21=True
                    print("You got a blackjack!")
                    sleep(1)
                else:
                    while inp!="h" and inp!="s" and inp!="d":
                        inp = input("Type \"h\" to hit, \"s\" to stand, or \"d\" to double\n").lower()
                        match inp:
                            case "s":
                                pass
                            case "h":
                                next_card, player_hand, player_aces=get_card(player_hand, player_aces)
                                print(f"You drew the {next_card}")
                                print(f"Value: {value_actual("p")}")
                            case "d":
                                next_card, player_hand, player_aces=get_card(player_hand, player_aces)
                                balance-=bet
                                bet*=2
                                print(f"Doubling down. New bet: ${bet:.2f}")
                                print(f"You drew the {next_card}")
                                print(f"Value: {value_actual("p")}")
                                inp="s"
                            case _:
                                print("Invalid input, please type \"h\" or \"s\" or \"d\"")
                    while value_actual("p")<22 and inp!="s":
                        inp=None
                        while inp!="h" and inp!="s":
                            inp = input("Type \"h\" to hit or \"s\" to stand\n").lower()
                            match inp:
                                case "s":
                                    pass
                                case "h":
                                    next_card, player_hand, player_aces=get_card(player_hand, player_aces)
                                    print(f"You drew the {next_card}")
                                    print(f"Value: {value_actual("p")}")
                                case _:
                                    print("Invalid input, please type \"h\" or \"s\"")
                print()
                if value_actual("p")>21:
                    print("You busted\n")
                    print(f"Dealer's second card was: {dealer_card_2}")
                    print(f"Value: {value_actual()}")
                else:
                    sleep(2)
                    print(f"Dealer's second card was: {dealer_card_2}")
                    print(f"Value: {value_actual()}")
                    if value_actual()==21:
                        print("\nDealer got a blackjack")
                    else:
                        while value_actual()<17:
                            sleep(1.75)
                            next_card, dealer_hand, dealer_aces=get_card(dealer_hand, dealer_aces)
                            print(f"Dealer drew the {next_card}")
                            print(f"Value: {value_actual()}")
                    print()
                    if value_actual()>21:
                        print("Dealer busted. You win!")
                        if _21:
                            print(f"+${bet*1.5:.2f}")
                            balance+=bet*2.5
                        else:
                            print(f"+${bet:.2f}")
                            balance+=bet*2
                    elif value_actual()>value_actual("p"):
                        print("You lost")
                    elif value_actual()<value_actual("p"):
                        print("You won!")
                        if _21:
                            print(f"+${bet*1.5:.2f}")
                            balance+=bet*2.5
                        else:
                            print(f"+${bet:.2f}")
                            balance+=bet*2
                    else:
                        print("Tie")
                        balance+=bet
                if file_perm:
                    with open("balance.txt", "w") as save:
                        save.write(str(balance))
                print()
            case "balance":
                print(f"Current balance: ${balance:.2f}")
            case "help":
                print("""Blackjack rules:
---
The goal of blackjack is to have your hand as close to 21 as possible without going over

Number cards are worth face value, face cards are all worth 10, and aces are worth either 11 or 1, depending on whether or not 11 would cause your current hand to exceed 21

If you go over 21, you bust and are immediately out of the game


The player and the dealer both start with 2 cards. One of the dealer's cards is face up, and the other is initially hidden
After looking at your cards, you can either hit (draw another card), or stand (end your turn). You can hit as many times as you want unless you go over 21
At the start of your turn, you can also choose to double down, which doubles your bet and lets you draw one more card before immediately ending your turn

The dealer follows specific rules regarding when he must hit or stand. If the dealer busts or has a lower hand than you, you win

Payout for a win is 1 to 1. If you start the game with a blackjack (a ten or face card and an ace), there is a 3 to 2 payout instead
---""")
            case "delete save" | "delete data":
                if file_perm:
                    delete("Are you sure you want to delete your saved data", True)
                else:
                    print("Unable to access save data")
                    delete("Delete data locally", False)
            case "quit":
                print(f"Final money amount: ${balance:.2f}")
                print("Bye!")
                break
            case _:
                print(f"\"{inp}\" is not a valid command")
        print("Type \"play\" to continue playing, \"balance\" to view current money amount, \"help\" for rules, \"delete save\" to delete data, or \"quit\" to quit")
