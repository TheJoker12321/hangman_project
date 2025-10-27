def init_state(secret: str, max_tries: int) -> dict:
    display = len(secret)
    new_dict = {"secret": secret, "display": "".join(["_" for _ in range(display)]),
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

# def is_won(state: dict) -> bool:


