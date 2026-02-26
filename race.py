from game_functions import*
from random import randrange

def start_rb():
    def win_loss_message(name, x=0,y=0.0):
        nonlocal scores, balance
        nonlocal tie1, tie2, tie3
        if scores[0][0]==name or scores[1][0]==name or name in tie1 or name in tie2:
            print(f"Your bet on {name.lower()} was a win!")
            print(f"+${x*(y-1):.2f}")
            balance+=x*y
        elif scores[2][0]==name or name in tie3:
            print(f"Your bet on {name.lower()} was a win!")
            y=(y-1)/2+1
            print(f"+${x*(y-1):.2f}")
            balance+=x*y
        else:
            print(f"Your bet on {name.lower()} was a loss")
        print()
    
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
    support=0
    support_text=None
    support_level=0
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
    print("""Hello, and welcome to race betting. Get started by placing a bet:
---
Type "bet" to start betting
Type "support" to support racers before the race
***Supports will be reset if you leave race betting
Type "balance" to view current money amount
Type "help" for more info on the racers, odds, and payouts
Type "delete save" to delete saved data from your computer
Type "quit" to quit
---""")
    while True:
        inp=input().lower()
        load(1)
        match inp:
            case "bet":
                r1=r2=r3=r4=r5=r6=r7=r8=False
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
                if support_level!=0:
                    print(f"Currently supporting {support_text}")
                while inp!="1" and inp!="2" and inp!="3" and inp!="4" and inp!="5" and inp!="6" and inp!="7" and inp!="8":
                    inp=input("Type a number 1-8 to bet on that racer\n").lower()
                    match inp:
                        case "1":
                            r1=True
                        case "2":
                            r2=True
                        case "3":
                            r3=True
                        case "4":
                            r4=True
                        case "5":
                            r5=True
                        case "6":
                            r6=True
                        case "7":
                            r7=True
                        case "8":
                            r8=True
                        case _:
                            print("Invalid input, please only type a number 1-8")
                load(3)
                scores=[["Racer 1", randrange(300)],["Racer 2", randrange(180)],["Racer 3", randrange(180)],["Racer 4", randrange(180)],["Racer 5", randrange(150)],["Racer 6", randrange(150)],["Racer 7", randrange(90)],["Racer 8", randrange(10)]]
                #for i in range(8):
                    #scores[i][1]=int(input()) Debugging
                if support_level!=0:
                    scores[support-1][1]+=5+5*support_level
                scores.sort(key=lambda score:score[1], reverse=True)
                tie1=[]
                tie2=[]
                tie3=[]
                for i in range(7):
                    if scores[i][0]!="Dead Heat":
                        for j in range(i+1, 8):
                            if scores[i][1]==scores[j][1]:
                                match i:
                                    case 0:
                                        if not scores[0][0] in tie1:
                                            tie1.append(scores[0][0])
                                        tie1.append(scores[j][0])
                                    case 1:
                                        if not scores[1][0] in tie2:
                                            tie2.append(scores[1][0])
                                        tie2.append(scores[j][0])
                                    case 2:
                                        if not scores[2][0] in tie3:
                                            tie3.append(scores[2][0])
                                        tie3.append(scores[j][0])
                                scores[i][0]+=", "+scores[j][0]
                                scores[j][0]="Dead Heat"
                print(f"""Results:
---
1st: {scores[0][0]}
2nd: {scores[1][0]}
3rd: {scores[2][0]}
4th: {scores[3][0]}
5th: {scores[4][0]}
6th: {scores[5][0]}
7th: {scores[6][0]}
8th: {scores[7][0]}
---""")
                print()
                if r1:
                    win_loss_message("Racer 1", bet,2)
                elif r2:
                    win_loss_message("Racer 2", bet,2.5)
                elif r3:
                    win_loss_message("Racer 3", bet,2.5)
                elif r4:
                    win_loss_message("Racer 4", bet,2.5)
                elif r5:
                    win_loss_message("Racer 5", bet,3)
                elif r6:
                    win_loss_message("Racer 6", bet,3)
                elif r7:
                    win_loss_message("Racer 7", bet,6)
                elif r8:
                    win_loss_message("Racer 8", bet,201)
                if file_perm:
                    with open("balance.txt", "w") as save:
                        save.write(str(balance))
                if support_level!=0:
                    print(f"Your support was appreciated from {support_text}\n")
                    support=0
                    support_text=None
                    support_level=0
            case "support":
                if balance>=100 and support_level==0:
                    print("Tier 1 supports cost $100, tier 2 supports cost $200, and tier 3 supports cost $300\n---")
                    skip=False
                    while inp!="1" and inp!="2" and inp!="3" and not skip:
                        inp=input("Type a number 1-3 to choose that tier of support, or type \"x\" to cancel\n").lower()
                        match inp:
                            case "1":
                                support_level=1
                                balance-=100
                            case "2":
                                if balance>=200:
                                    support_level=2
                                    balance-=200
                                else:
                                    print("Cannot purchase tier 2 support due to balance")
                                    inp=None
                            case "3":
                                if balance>=300:
                                    support_level=3
                                    balance-=300
                                else:
                                    print("Cannot purchase tier 3 support due to balance")
                                    inp=None
                            case "x":
                                skip=True
                                load(1)
                            case _:
                                print("Invalid input, please type a number 1-3 or \"x\"")
                    if not skip:
                        if file_perm:
                            with open("balance.txt", "w") as save:
                                save.write(str(balance))
                        inp=None
                        while inp!="1" and inp!="2" and inp!="3" and inp!="4" and inp!="5" and inp!="6" and inp!="7" and inp!="8":
                            inp=input("Type a number 1-8 to support that racer\n").lower()
                            match inp:
                                case "1":
                                    support=1
                                    support_text="Daiwa Scarlet (racer 1)"
                                case "2":
                                    support=2
                                    support_text="Gold Ship (racer 2)"
                                case "3":
                                    support=3
                                    support_text="Slow Dancer (racer 3)"
                                case "4":
                                    support=4
                                    support_text="Silver Bullet (racer 4)"
                                case "5":
                                    support=5
                                    support_text="Special Week (racer 5)"
                                case "6":
                                    support=6
                                    support_text="Vodka (racer 6)"
                                case "7":
                                    support=7
                                    support_text="Agnes Tachyon (racer 7)"
                                case "8":
                                    support=8
                                    support_text="Haru Urara (racer 8)"
                                case _:
                                    print("Invalid input, please type a number 1-8")
                        load(1)
                        print(f"Sent level {support_level} support to {support_text}!")
                elif support_level!=0:
                    print("Already supporting a racer")
                else:
                    print("Insufficient balance to support racers")
            case "balance":
                print(f"Current balance: ${balance:.2f}")
            case "help":
                print("""Racer odds and payouts:
---
Racer 1, Daiwa Scarlet, is energetic and young. Very high odds to win, 1 to 1 payout
Racers 2, 3, and 4, Gold Ship, Slow Dancer, and Silver Bullet, are experienced racers. Decently high odds to win, 3 to 2 payout
Racers 5 and 6, Special Week and Vodka, are a bit inexperienced. Still good odds of winning, 2 to 1 payout
Racer 7, Agnes Tachyon, is clumsy. Worse odds of winning than the other racers, 5 to 1 payout
Racer 8, Haru Urara, is very slow. Extremely bad odds to win, due to very low odds of winning there is a 200 to 1 payout

Full payouts are awarded if your racer finishes in 1st or 2nd
Payouts are halved if your racer finishes in 3rd
No payouts are awarded for placements below 3rd


If you choose to support a racer before the race, his/her odds of winning are boosted slightly. Supports run on a 3-tier system
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
        print("Type \"bet\" to place another bet, \"support\" to support a racer, \"balance\" to view current money amount, \"help\" for info on racer odds and payouts, \"delete save\" to delete data, or \"quit\" to quit")