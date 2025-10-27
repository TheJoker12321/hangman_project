from hangman.words import choose_secret_word
from hangman.game import *
from hangman.io import *

def play(words: list[str], max_tries: int = 6) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)
    print_status(state)
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
                print_status(state)
            else:
                state["guessed"].add(letter)
                state["wrong_guesses"] += 1
                print("This letter is not on the list")
                print_status(state)
        if "_" not in state["display"]:
            break
    print_result(state)

if __name__ == "__main__":
    word = ["בננה", "תפוח", "חציל", "עגבניה", "מלפפון", "מחשב"]
    play(word)