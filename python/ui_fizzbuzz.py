"""
A version of FizzBuzz that prompts the user for the rules before running.
"""


_rules: dict[int, str] = {}

def ui_fizzbuzz(max_number: int):
    _get_user_input()
    for number in range(1, max_number + 1):
        _play_game(number)
    return

def _get_user_input():
    print("Rules should be entered as : number, word. Invalid inputs are ignored.")
    print("Example: 3, Fizz")
    print("Hit return with no input when done adding rules.")
    while True: #rely on empty input to end loop
        user_input = input("enter a rule: ")
        if not user_input:
            break

        parts = user_input.split(",")
        try:
            _rules[int(parts[0].strip())] = parts[1].strip()
        except Exception:
            # noop - ignoring invalid inputs that don't parse
            continue 
    return

def _play_game(number: int):
    output: str = ""
    for factor, word in _rules.items():
        output += (not(number % factor)) * word
    print(output or number)
