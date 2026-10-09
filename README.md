Number Analyzer

A beginner-friendly Python program that determines whether a number is positive, negative, or zero, and checks whether it is even or odd.

About the Project

I am a freshman undergraduate learning Python. This project is part of my programming practice and helps me understand conditional statements, comparison operators, the modulo operator, and formatted output.

What the Program Does

Asks the user to enter an integer.

Identifies whether the number is positive, negative, or zero.

Checks whether the number is even or odd.

Displays the results.

Concepts Used

input()

int()

Variables

if / elif / else

Comparison operators

Modulo operator (%)

f-strings

Code

number = int(input("enter your number:"))

if number > 0:
    result = "positive"
elif number < 0:
    result = "negative"
else:
    result = "zero"

if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"

print("===== NUMBER ANALYZER =====")
print(f"Number: {number}")
print(f"Type: {result}")
print(f"Parity: {parity}")

Example

enter your number: 8
===== NUMBER ANALYZER =====
Number: 8
Type: positive
Parity: even

Requirements

Python 3.x

No external libraries

How to Run

Run the program from a terminal:

python "number analyzer.py"

Enter an integer when prompted.

Learning Status

Level: Beginner
Project Type: Python Practice Project
Focus: Conditions, comparisons, modulo, and formatted output

Future Improvements

Handle invalid input.

Let the user analyze multiple numbers in one run.

Move the analysis into a function.

Add more number properties, such as whether a number is divisible by 3 or 5.

Author

A freshman undergraduate learning Python and developing programming fundamentals through hands-on projects.
