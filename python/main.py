"""
This module is a launching point for the multiple versions of fizzbuzz that I have tried in python.
"""

import basic_fizzbuzz
import extensible_fizzbuzz
import four_lines_fizzbuzz 
import oneline_fizzbuzz
import ui_fizzbuzz

VERSIONS: list[dict]= [
    {
        "label": "basic",
        "method": basic_fizzbuzz.basic_fizzbuzz
    },
    {
        "label": "one-liner",
        "method": oneline_fizzbuzz.oneline_fizzbuzz
    },
    {
        "label": "extensible",
        "method": extensible_fizzbuzz.extensible_fizzbuzz
    },
    {
        "label": "four lines",
        "method": four_lines_fizzbuzz.four_line_fizzbuzz
    },
    {
        "label": "UI FizzBuzz",
        "method": ui_fizzbuzz.ui_fizzbuzz
    }
]

MAX_NUMBER: int = 45

def main() -> int:
    display_menu()
    selection = get_user_selection()
    version = VERSIONS[selection]
    print(f"\nRunning: {version['label']}")
    version['method'](MAX_NUMBER)
    return 0

def display_menu():
    print("FizzBuzz Versions:")
    for version in VERSIONS:
        print(f"{VERSIONS.index(version)}: {version.get("label")}")
    pass

def get_user_selection() -> int:
    selection = input("Selection:[0] ")
    if not selection:
        return 0
    try:
        return int(selection)
    except:
        return 0

if __name__ == "__main__":
    main()
