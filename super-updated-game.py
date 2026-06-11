import random

number = random.randint(1, 10)
attempts = 3

print("У тебе є 3 спроби 🎯")

while attempts > 0:
    guess = int(input("Вгадай число (1–10): "))

    if guess == number:
        print("Правильно! 🎉 Ти переміг!")
        break
    else:
        attempts -= 1
        print("Ні 😅 Залишилось спроб:", attempts)

        if guess < number:
            print("⬆️ Більше")
        else:
            print("⬇️ Менше")

if attempts == 0:
    print("Гру закінчено ❌ Правильне число було:", number)
