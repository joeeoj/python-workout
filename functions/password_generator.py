import random
from typing import Callable


def create_password_generator(seed: str) -> Callable[[int], str]:
    """That string will return a function, which itself takes an integer argument. Will return a password of the
    specified length, using the string from which it was created."""
    def gen_pass(length: int) -> str:
        return ''.join(random.choices(seed, k=length))

    return gen_pass
