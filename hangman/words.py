import random
def choose_secret_word(words: list[str]) -> str:
    new_word = random.choice(words)[::-1]
    return new_word