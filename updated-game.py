import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Вгадай число від 1 до 10: "))

    if guess < number:
        print("Більше ⬆️")
    elif guess > number:
        print("Менше ⬇️")
    else:
        print("Правильно! 🎉")
