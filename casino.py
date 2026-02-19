from game_functions import*
import roulette

def print_guide():
    print("""---
Type \"r\" to start roulette
Type \"quit\" to quit
More games coming soon
---""") #Easy game ideas: Blackjack, slots, etc.

clear()
print("Welcome to the Casino!!")
print_guide()
while True:
    inp=input().lower()
    load(1)
    match inp:
        case "r":
            roulette.start_r()
        case "quit":
            print("Bye!")
            break
        case _:
            print(f"\"{inp}\" is not a valid command")
    print_guide()