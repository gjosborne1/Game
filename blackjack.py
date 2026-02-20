from game_functions import*
from random import randrange

def start_b():
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
                #PUT CODE FOR GAME HERE  <---
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

Payout for a win is 1 to 1. If you start the game with a blackjack (a face card and an ace), there is a 3 to 2 payout instead
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