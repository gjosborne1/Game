from game_functions import*
from random import randrange

def start_s():
    def symbol(index, bonus=False):
        if bonus:
            position=index%6
        else:
            position=index%9
        match position:
            case 0:
                return " X "
            case 1:
                return " ☆ "
            case 2:
                return " β "
            case 3:
                return " ẟ "
            case 4:
                return " $ "
            case 5:
                return " 7 "
            case 6:
                return " 2x"
            case 7:
                return " 3x"
            case 8:
                return " 5x"

    def win(amount, mult, jackpot=False):
        print("You win!")
        if jackpot:
            print("Jackpot!")
        print(f"+${amount*(mult-1):.2f}")
        nonlocal balance; balance+=amount*mult

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
    print("""Hello, and welcome to slots. Ready to start playing?
---
Type "play" to start the machine
Type "balance" to view current money amount
Type "help" for info on the symbols, multipliers, and payouts of this machine
Type "delete save" to delete saved data from your computer
Type "quit" to quit
---""")
    while True:
        inp=input().lower()
        load(1)
        match inp:
            case "play":
                bet=0
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
                    print("Insufficient balance to play slots")
                if bet>0:
                    slot_1=randrange(9)
                    slot_2=randrange(9)
                    slot_3=randrange(9)
                    balance-=bet
                    print(" $  $  $ ", end="\n"*terminal_height())
                    sleep(.5)
                    for i in range(10):
                        clear()
                        symbol_1=symbol(slot_1+i)
                        symbol_2=symbol(slot_2+i)
                        symbol_3=symbol(slot_3+i)
                        print(f"{symbol_1}{symbol_2}{symbol_3}", end="\n"*terminal_height())
                        sleep(.12)
                    for i in range(10):
                        clear()
                        symbol_1=symbol(slot_1+10+i)
                        symbol_2=symbol(slot_2+10+i)
                        symbol_3=symbol(slot_3+10+i)
                        print(f"{symbol_1}{symbol_2}{symbol_3}", end="\n"*terminal_height())
                        sleep(.12)
                    for i in range(10):
                        clear()
                        symbol_2=symbol(slot_2+20+i)
                        symbol_3=symbol(slot_3+20+i)
                        print(f"{symbol_1}{symbol_2}{symbol_3}", end="\n"*terminal_height())
                        sleep(.12)
                    for i in range(10):
                        clear()
                        symbol_3=symbol(slot_3+30+i)
                        if i<9:
                            print(f"{symbol_1}{symbol_2}{symbol_3}", end="\n"*terminal_height())
                            sleep(.12)
                        else:
                            print(f"{symbol_1}{symbol_2}{symbol_3}")
                    print()
                    if symbol_1==symbol_2==symbol_3:
                        match symbol_1:
                            case " X ":
                                print(f"${bet/2:.2f} returned of original bet")
                                balance+=bet/2
                            case " ☆ ":
                                win(bet, 2)
                            case " β " | " ẟ ":
                                win(bet, 6)
                            case " $ ":
                                win(bet, 21, True)
                            case " 7 ":
                                win(bet, 51, True)
                            case " 2x":
                                print("2x multiplier placeholder")
                            case " 3x":
                                print("3x multiplier placeholder")
                            case " 5x":
                                print("5x multiplier placeholder")
                    elif symbol_1==" ☆ " or symbol_2==" ☆ " or symbol_3==" ☆ ":
                        print(f"${bet:.2f} returned of original bet")
                        balance+=bet
                    if file_perm:
                        with open("balance.txt", "w") as save:
                            save.write(str(balance))
            case "balance":
                print(f"Current balance: ${balance:.2f}")
            case "help":
                print("""The slot machine has the following symbols and payouts:
---
Any 3 random symbols: No payout
XXX: Half of bet returned (not affected by multipliers)
☆ or ☆☆ and random symbols: Bet returned (not affected by multipliers)
☆☆☆: 1 to 1 payout
βββ or ẟẟẟ: 5 to 1 payout
$$$: 20 to 1 payout
777: 50 to 1 payout
2x2x2x: Automatically spin again with 2x all payouts
3x3x3x: Automatically spin again with 3x all payouts
5x5x5x: Automatically spin again with 5x all payouts
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
        print("Type \"play\" to continue spinning, \"balance\" to view current money amount, \"help\" for symbols and payout info, \"delete save\" to delete data, or \"quit\" to quit")