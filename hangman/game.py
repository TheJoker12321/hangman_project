def init_state(secret: str, max_tries: int) -> dict:
    display = len(secret)
    new_dict = {"secret": secret, "display": ["_" for _ in range(display)],
                "guessed": set(),"wrong_guesses": 0, "max_tries": max_tries }
    return new_dict

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) != 1:
        raise ValueError("You must type only one letter")
    if ch in guessed:
        return False, f"{ch} has already been deciphered "
    return True, f"{ch} was not guessed"


def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        return True
    return False

def is_won(state: dict) -> bool:
    letter_word = [i for i in state["secret"]]
    for i in letter_word:
        if i not in state["guessed"]:
            return False
    return True

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    return False

def render_display(state: dict) -> str:
    return "".join(state["display"])

def render_summary(state: dict) -> str:
    secret_word = state["secret"]
    word_guessed = " , ".join(state["guessed"])
    return secret_word + " " + word_guessed









