def init_state(secret: str, max_tries: int) -> dict:
    display = len(secret)
    new_dict = {"secret": secret, "display": "".join(["_" for _ in range(display)]),
                "guessed": set(),"wrong_guesses": 0, "max_tries": max_tries }
    return new_dict

