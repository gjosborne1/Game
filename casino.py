from game_functions import*
import roulette
import blackjack
import slots
import d_or_n
import race

def print_guide():
    print("""---
Type \"r\" to start roulette
Type \"b\" to start blackjack
Type \"s\" to start slots
Type \"d\" to start double or nothing
Type \"rb\" to start race betting
Type \"quit\" to quit
---""")

def main():
    clear()
    print("Welcome to the Casino!!")
    print_guide()
    while True:
        inp=input().lower()
        load(1)
        match inp:
            case "r":
                roulette.start_r()
            case "b":
                blackjack.start_b()
            case "s":
                slots.start_s()
            case "d":
                d_or_n.start_d()
            case "rb":
                race.start_rb()
            case "quit":
                print("Bye!")
                break
            case _:
                print(f"\"{inp}\" is not a valid command")
        print_guide()

main()