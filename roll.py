from game_functions import*
from random import randrange

def start_dr():
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
    print("""Hello, and welcome to deathroll. Ready to start gambling?
---
Type "play" to start rolling
Type "balance" to view current money amount
Type "help" for an explanation of how deathroll works
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
                num_range=1000
                rolled=None
                print("Type \"roll\" to take your turn\n---")
                while rolled!=0:
                    inp=None
                    while inp!="roll":
                        inp=input(f"Your turn. Current range: 1-{num_range}\n").lower()
                        if inp!="roll":
                            print("Invalid input, please type \"roll\" to take your turn")
                        else:
                            rolled=randrange(num_range)
                            num_range=rolled+1
                            print(f"Rolled a {rolled+1}\n")
                    if rolled==0:
                        print("You lost")
                    else:
                        sleep(1.75)
                        print(f"Player 2's turn. Current range: 1-{num_range}")
                        sleep(2.5)
                        rolled=randrange(num_range)
                        num_range=rolled+1
                        print(f"Player 2 rolled a {rolled+1}\n")
                        if rolled==0:
                            print("You won!")
                            print(f"+${bet:.2f}")
                            balance+=bet*2
                        else:
                            sleep(1.75)
                if file_perm:
                    with open("balance.txt", "w") as save:
                        save.write(str(balance))
                print()
            case "balance":
                print(f"Current balance: ${balance:.2f}")
            case "help":
                print("""Deathroll rules:
---
After making a bet, both players will take turns rolling random numbers, starting between 1 and 1,000

Whoever rolls a 1 first loses, and must pay the other player the agreed upon bet

Each time a player rolls a number, that number becomes the upper limit for the next roll
For example, if player 1 rolls an 800 on the first roll, player 2 now rolls 1-800, and so on until the game ends
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