import random
# generate random values in Python using random library

number1 = random.random()
# Select a random floating-point number between 0 and 1
number1 = number1*100
print("\n",number1, "\n")


# Creates two random integers within two the choosing range 
number2 = random.randint(0, 1000)
print(number2)
number3 = random.randint(0, 1000)
print(number3)
newrand = number2/number3
print(newrand, "\n")


# Selects a random whole number between 0 and 9
number4 = random.randint(0, 9)
print(number4)