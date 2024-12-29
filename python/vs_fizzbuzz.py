"""
An implementation of FizzBuzz that alows a player to play against the computer rather than just viewing the output.
"""

import sys
from typing import Any


RULES:dict[int, str] = {
    3: "Fizz",
    5: "Buzz",
}

CONF: dict[str, Any] = {
    "playerFirst": True,
    "level": 0
}

QUIT = False

def vs_fizzbuzz(max_number: int):
    _display_menu()
    _play(max_number)
    # TODO: computer's turn should print in blue
    # TODO: player's turn will clear and reprint in either red or green for write or wrong answers.
    return

def _display_menu():
    """
    displays a menu for setting up the game
    """
    print("Rules:")
    print("""
    Durring your turn, if the next number is evenly divisible by
    one of the numbers below, enter the matching word. If
    more than one matches, combine the words. Otherwise enter the number.
    """)
    for num, word in RULES.items():
        print(f"{num} -> {word}")
    print()
    return

def _play(max_number:int):
    player_turn = False
    for number in range(1, max_number+ 1) :
        if QUIT:
            return
        if player_turn:
            _user_turn(number)
        else :
            _computer_turn(number)
        player_turn = not player_turn  # flip the value each turn

def _user_turn(number: int):
    correct_answer = _get_answer(number)
    global QUIT
    try:
        players_answer = input()
    except KeyboardInterrupt:
        QUIT = True
        prError("Bye!")
        return

    if players_answer != correct_answer :
        _delete_line()
        prError(f"Wrong! - {correct_answer}")
    return

def _computer_turn(number: int):
    computers_answer = _get_answer(number)
    print(computers_answer)
    return

def _get_answer(number: int) -> str:
    """
    gets the answer the computer should use on it's and to check against
    the user's input to confirm if it is correct or not.
    """

    output: str = ""
    for factor, word in RULES.items():
        output += (not number % factor) * word

    return output or str(number)


def _delete_line():
    """
    clears the last line in stdout
    """

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def prError(msg: str):
    print(f"\033[91m{msg}\033[0m")
