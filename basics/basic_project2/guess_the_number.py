import random

print("Advinhe um número de 1 a 1000")
number = random.randint(1,1000)

def guess_input():
    guess_str = input()
    try:
        guess = int(guess_str)
        return guess
    except ValueError:
        print("Digite um número válido.")

guess = 0
guess_input()

while guess != number:
    guess = guess_input()
    if guess < number:
        print("Your guess is low, try again")
    elif guess > number:
        print("Your guess is high, try again")  
    else:
        print(f"Nice! The number is {number}")
