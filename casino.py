from game_functions import*
import roulette
import blackjack

def print_guide():
    print("""---
Type \"r\" to start roulette
Type \"b\" to start blackjack
Type \"s\" to start slots
Type \"quit\" to quit
More games coming soon
---""")

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
            print("Coming soon")
        case "quit":
            print("Bye!")
            break
        case _:
            print(f"\"{inp}\" is not a valid command")
    print_guide()