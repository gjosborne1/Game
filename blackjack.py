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
                print() #DO THIS
            case "balance":
                print(f"Current balance: ${balance:.2f}")
            case "help":
                print() #Explanation goes here
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