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
