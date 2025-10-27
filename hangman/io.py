from hangman.game import *

def prompt_guess() -> str:
    ch = input("guess a char: ")
    return ch

def print_status(state: dict) -> None:
    print(render_display(state))
    while not is_lost(state):
        letter = prompt_guess()
        if not validate_guess(letter, state["guessed"])[0]:
            print(validate_guess(letter, state["guessed"])[1])
            continue
        else:
            if apply_guess(state, letter):
                index_ch = []
                for i, j in enumerate(state["secret"]):
                    if letter == j:
                        index_ch.append(i)
                for i in index_ch:
                    state["display"][i] = letter
                state["guessed"].add(letter)
                print(render_display(state))
            else:
                state["guessed"].add(letter)
                state["wrong_guesses"] += 1
                print("This letter is not on the list")
        if "_" not in state["display"]:
            break

def print_result(state: dict) -> None:
    if "_" not in state["display"]:
        print("You won!!!")
    else:
        print("You lose!!")
    print("The word is: ", render_summary(state))




