"""
A very basic and "typical" FizzBuzz with nothing fancy.

Explicitly checking for every possible match for every possible output.
"""

def basic_fizzbuzz(max_number: int = 30) -> None:
    for number in range(1, max_number + 1) :
        if number  % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
