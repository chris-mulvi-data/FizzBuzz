"""
An extensible version of FizzBuzz that can have rules added or removed.
"""

_rules: dict[int, str] = {
    3: "Fizz",
    5: "Buzz",
    7: "Bazz",
}

def extensible_fizzbuzz(max_number: int = 30):
    for number in range(1, max_number + 1):
        print(_play_game(number))
    return

def _play_game(number:int) -> str:
    output = ""
    for k, v in _rules.items():
        if number % k == 0:
            output += v

    return output or str(number)
