from hangman.game import *

def prompt_guess() -> str:
    ch = input("guess a char: ")
    return ch

def print_status(state: dict) -> None:
    print(render_display(state))
    if len(state["guessed"]) > 0:
        print("guessed", state["guessed"])
    print("Remaining guesses: ", state["max_tries"] - state["wrong_guesses"])

def print_result(state: dict) -> None:
    if "_" not in state["display"]:
        print("You won!!!")
    else:
        print("You lose!!")
    print("The word is: ", render_summary(state))




