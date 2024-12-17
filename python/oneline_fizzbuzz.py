"""
A one-liner wrapped in a function to make it callable from the main menu.

Uses list comprehension and string multiplication to produce the output.
"""

def oneline_fizzbuzz(max_number:int = 30):
    print("\n".join([(not (i % 3))*"Fizz" + (not(i % 5))* "Buzz" or str(i) for i in range(1, max_number+1)]))
