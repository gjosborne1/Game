from game_functions import*
from random import randrange

def start_d():
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
    print("""Hello, and welcome to double or nothing. Ready to test your luck?
---
Type "play" to start playing
Type "balance" to view current money amount
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
                print("You will be continually asked whether you want to risk your money. Type \"y\" to risk doubling your bet or losing it all, or type \"n\" to tap out\n---")
                game_loop=True
                while game_loop:
                    inp=None
                    while inp!="y" and inp!="n":
                        inp=input(f"Risk your money? Current bet: ${bet:.2f}\n").lower()
                        match inp:
                            case "y":
                                win=randrange(2)
                                if win==1:
                                    print("You win!")
                                    print(f"+${bet:.2f}\n")
                                    balance+=bet
                                    bet*=2
                                else:
                                    print("You lose")
                                    balance-=bet
                                    game_loop=False
                            case "n":
                                game_loop=False
                            case _:
                                print("Invalid input, please type \"y\" to risk or \"n\" to tap out")
                if file_perm:
                    with open("balance.txt", "w") as save:
                        save.write(str(balance))
                print()
            case "balance":
                print(f"Current balance: ${balance:.2f}")
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
        print("Type \"play\" to play again, \"balance\" to view current money amount, \"delete save\" to delete data, or \"quit\" to quit")