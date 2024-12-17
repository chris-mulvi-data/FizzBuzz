"""
A 4 line version of FizzBuzz
"""

def four_line_fizzbuzz(max_number: int = 30):
    for number in range(1, max_number + 1):
        output = (not (number % 3)) * "Fizz" or ""
        output += (not (number % 5)) * "Buzz" or ""
        print(output or number)
