from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


STANDARD_USER = User("standard_user", "secret_sauce")
LOCKED_OUT_USER = User("locked_out_user", "secret_sauce")
PERFORMANCE_GLITCH_USER = User("performance_glitch_user", "secret_sauce")

INVALID_PASSWORD_USER = User("standard_user", "wrong_password")
EMPTY_USER = User("", "")
