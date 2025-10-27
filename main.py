from hangman.words import choose_secret_word
from hangman.game import *
from hangman.io import *
if __name__ == "__main__":
    word = (choose_secret_word(["בננה", "תפוח", "חציל", "עגבניה", "מלפפון", "מחשב"]))
    status_game = init_state(word, 6)
    print_status(status_game)
    print_result(status_game)