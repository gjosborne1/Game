from game_functions import*
from random import randrange

def start_r():
    def check_balance(x,y,z, negative_bet):
        if z-x*(y+1)<0 and not negative_bet:
            print("Cannot make anymore bets due to balance")
            return False
        else:
            nonlocal made_bet; made_bet+=1
            nonlocal negative; negative=False
            return True
    
    def msg(bet_type, w_l="l", x=0,y=0):
        if w_l=="w":
            print(f"Your bet on {bet_type} was a win!")
            print(f"+${x*(y-1):.2f}")
            nonlocal balance; balance+=x*y
        else:
            print(f"Your bet on {bet_type} was a loss")
    
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
    print("""Hello, and welcome to roulette. Would you like to place a bet?
---
Type "bet" to start betting
Type "balance" to view current money amount
Type "help" for more info on how betting works
Type "delete save" to delete saved data from your computer
Type "quit" to quit
---""")
    while True:
        inp=input().lower()
        load(1)
        match inp:
            case "bet":
                num=randrange(38)                                                                               #Gets number and initializes associated variables
                if num==37:
                    num_actual="00"
                else:
                    num_actual=str(num)
                if num==0 or num==37:
                    odd_even="neither odd nor even"
                    color="green"
                    row=0; half=0; third=0
                else:
                    if num%2==0:
                        odd_even="even"
                    else:
                        odd_even="odd"
                    if num<11 or 18<num<29:
                        if odd_even=="even":
                            color="black"
                        else:
                            color="red"
                    else:
                        if odd_even=="even":
                            color="red"
                        else:
                            color="black"
                    if num%3==0:
                        row=3
                    else:
                        row=num%3
                    if num<19:
                        half=1
                    else:
                        half=2
                    if num<13:
                        third=1
                    elif num<25:
                        third=2
                    else:
                        third=3
                odd=even=red=black=row1=row2=row3=half1=half2=third1=third2=third3=single=_0=_00=False          #Gets user inputs for bets
                single_list=[""]*36
                bet=100
                if balance>=.01:
                    negative=False
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
                    negative=True
                    print("No money to bet. Bet automatically set to $100")
                print("You will be asked to make certain bets in order; each individual bet can either win or lose money. If you do NOT wish to make the bet, type \"n\" to move on:")
                print("(Type \"x\" at any time to cancel bets or finish betting early)\n---")
                made_bet=0
                skip=False
                while inp!="o" and inp!="e" and inp!="n" and not skip:
                    inp = input("Type \"o\" to bet on odd or \"e\" to bet on even\n").lower()
                    match inp:
                        case "o":
                            odd=check_balance(bet,made_bet,balance, negative)
                        case "e":
                            even=check_balance(bet,made_bet,balance, negative)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"o\" or \"e\" or move on by typing \"n\"")
                inp=None
                while inp!="r" and inp!="b" and inp!="n" and not skip:
                    inp=input("Type \"r\" to bet on red or \"b\" to bet on black\n").lower()
                    match inp:
                        case "r":
                            red=check_balance(bet,made_bet,balance, negative)
                        case "b":
                            black=check_balance(bet,made_bet,balance, negative)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"r\" or \"b\" or move on by typing \"n\"")
                inp=None
                while inp!="1" and inp!="2" and inp!="3" and inp!="n" and not skip:
                    inp = input("Type \"1\" to bet on column 1, \"2\" to bet on column 2, or \"3\" to bet on column 3\n").lower()
                    match inp:
                        case "1":
                            row1=check_balance(bet,made_bet,balance, negative)
                        case "2":
                            row2=check_balance(bet,made_bet,balance, negative)
                        case "3":
                            row3=check_balance(bet,made_bet,balance, negative)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"1\" or \"2\" or \"3\" or move on by typing \"n\"")
                inp=None
                while inp!="1" and inp!="2" and inp!="n" and not skip:
                    inp=input("Type \"1\" to bet on half 1 (1-18) or \"2\" to bet on half 2 (19-36)\n").lower()
                    match inp:
                        case "1":
                            half1=check_balance(bet,made_bet,balance, negative)
                        case "2":
                            half2=check_balance(bet,made_bet,balance, negative)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"1\" or \"2\" or move on by typing \"n\"")
                inp=None
                while inp!="1" and inp!="2" and inp!="3" and inp!="n" and not skip:
                    inp = input("Type \"1\" to bet on third 1 (1st dozen), \"2\" to bet on third 2 (2nd dozen), or \"3\" to bet on third 3 (3rd dozen)\n").lower()
                    match inp:
                        case "1":
                            third1=check_balance(bet,made_bet,balance, negative)
                        case "2":
                            third2=check_balance(bet,made_bet,balance, negative)
                        case "3":
                            third3=check_balance(bet,made_bet,balance, negative)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"1\" or \"2\" or \"3\" or move on by typing \"n\"")
                inp=None
                counter=0
                while counter<36 and inp!="n" and not skip:
                    inp = input("Type a number between 1 and 36 to bet on that number:\n")
                    match inp:
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            try:
                                inp = int(inp)
                            except ValueError:
                                print("Invalid input, please type a number between 1 and 36 or move on by typing \"n\"")
                            else:
                                if not 0<inp<37:
                                    print("Invalid input, please type a number between 1 and 36 or move on by typing \"n\"")
                                elif str(inp) in single_list:
                                    print("Cannot bet on a number twice")
                                else:
                                    single=check_balance(bet,made_bet,balance, negative)
                                    if single:
                                        single_list[counter]=str(inp)
                                        counter+=1
                                    else:
                                        counter=36
                                        if single_list[0]!="":
                                            single=True
                inp=None
                while inp!="y" and inp!="n" and not skip:
                    inp = input("Type \"y\" to bet on 0\n").lower()
                    match inp:
                        case "y":
                            _0=check_balance(bet,made_bet,balance, negative)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"y\" or move on by typing \"n\"")
                inp=None
                while inp!="y" and inp!="n" and not skip:
                    inp = input("Type \"y\" to bet on 00\n").lower()
                    match inp:
                        case "y":
                            _00=check_balance(bet,made_bet,balance, negative)
                            if not _00:
                                sleep(2)
                        case "n":
                            pass
                        case "x":
                            skip=True
                        case _:
                            print("Invalid input, please type \"y\" or move on by typing \"n\"")
                if skip and made_bet!=0:
                    inp=None
                    while inp!="y" and inp!="n":
                        inp = input("Type \"y\" to continue to results or \"n\" to cancel bets\n").lower()
                        match inp:
                            case "y":
                                pass
                            case "n":
                                made_bet=0
                            case _:
                                print("Invalid input, please type \"y\" or \"n\"")
                if made_bet>0:                                                                                  #Checks win conditions
                    balance-=bet*made_bet
                    load()
                    print(f"Landed on: {num_actual}")
                    print(f"{num_actual} is {odd_even}")
                    print(f"{num_actual} is {color}")
                    if row!=0:
                        print(f"{num_actual} is in column {row}")
                        print(f"{num_actual} is in half {half}")
                        print(f"{num_actual} is in third {third}")
                    print()
                    if odd:
                        if odd_even=="odd":
                            msg("odds", "w", bet,2)
                        else:
                            msg("odds")
                    if even:
                        if odd_even=="even":
                            msg("evens", "w", bet,2)
                        else:
                            msg("evens")
                    if red:
                        if color=="red":
                            msg("reds", "w", bet,2)
                        else:
                            msg("reds")
                    if black:
                        if color=="black":
                            msg("blacks", "w", bet,2)
                        else:
                            msg("blacks")
                    if row1:
                        if row==1:
                            msg("column 1", "w", bet,3)
                        else:
                            msg("column 1")
                    if row2:
                        if row==2:
                            msg("column 2", "w", bet,3)
                        else:
                            msg("column 2")
                    if row3:
                        if row==3:
                            msg("column 3", "w", bet,3)
                        else:
                            msg("column 3")
                    if half1:
                        if half==1:
                            msg("half 1", "w", bet,2)
                        else:
                            msg("half 1")
                    if half2:
                        if half==2:
                            msg("half 2", "w", bet,2)
                        else:
                            msg("half 2")
                    if third1:
                        if third==1:
                            msg("third 1", "w", bet,3)
                        else:
                            msg("third 1")
                    if third2:
                        if third==2:
                            msg("third 2", "w", bet,3)
                        else:
                            msg("third 2")
                    if third3:
                        if third==3:
                            msg("third 3", "w", bet,3)
                        else:
                            msg("third 3")
                    if single:
                        counter=0
                        while counter<36 and single_list[counter]!="":
                            if num_actual==single_list[counter]:
                                msg(single_list[counter], "w", bet,36)
                            else:
                                msg(single_list[counter])
                            counter+=1
                    if _0:
                        if num_actual=="0":
                            msg("0", "w", bet,36)
                        else:
                            msg("0")
                    if _00:
                        if num_actual=="00":
                            msg("00", "w", bet,36)
                        else:
                            msg("00")
                    print()
                    if file_perm:
                        with open("balance.txt", "w") as save:
                            save.write(str(balance))
                else:
                    clear()
                    print("No bets were made")
            case "balance":
                print(f"Current balance: ${balance:.2f}")
            case "help":
                print("""Available bets:
---
Odd/Even: Bet on every odd number or every even number, 1 to 1 payout
Red/Black: Bet on every red number or every black number, 1 to 1 payout
Column: Bet on the entire first, second, or third horizontal row on the table, 2 to 1 payout
1-18 or 19-36: Bet on the entire first or second vertical half of the table, 1 to 1 payout
Dozen: Bet on the entire first, second, or third vertical third of the table, 2 to 1 payout
Single: Bet on one number on the table, 35 to 1 payout. Multiple numbers can be bet on at the same time!

The table layout is as follows:
3r  6b  9r  12r  15b  18r  21r  24b  27r  30r  33b  36r   column 3
2b  5r  8b  11b  14r  17b  20b  23r  26b  29b  32r  35b   column 2
1r  4b  7r  10b  13b  16r  19r  22b  25r  28b  31b  34r   column 1
     third 1    |     third 2      |      third 3      |
         half 1           |          half 2            |

The table also includes a green 0 and a green 00, which will each have a 35 to 1 payout
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
        print("Type \"bet\" to continue playing, \"balance\" to view current money amount, \"help\" for info on betting, \"delete save\" to delete data, or \"quit\" to quit")