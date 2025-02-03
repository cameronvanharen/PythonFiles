import random

def guess_number():
    x = random.randint(1,20)
    return x

number = guess_number()
guess = int(input("guess number: "))
while number != guess:
    if guess < number:
        print("Number is higher")
    elif guess > number:
        print("Number is lower")
    guess = int(input("guess number: "))
print("guess was correct!") 