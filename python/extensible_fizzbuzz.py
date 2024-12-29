"""
An extensible version of FizzBuzz that can have rules added or removed.
"""
import sys
import time

_rules: dict[int, str] = {
    3: "Fizz",
    5: "Buzz",
    7: "Bazz",
}

def extensible_fizzbuzz(max_number: int = 30):
    for number in range(1, max_number + 1):
        print(_play_game(number), end="\r", flush=True)
        time.sleep(.2)
        _delete_line()
    return

def _play_game(number:int) -> str:
    output = ""
    for k, v in _rules.items():
        if number % k == 0:
            output += v

    return output or str(number)

def _delete_line():
    """
    clears the last line in stdout
    """

    #cursor up one line
    # sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

