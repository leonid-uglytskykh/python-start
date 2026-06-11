import random

while True:
    print("\n=== GAME HUB ===")
    print("1. Вгадай число")
    print("2. Вийти")

    choice = input("Вибери опцію: ")

    if choice == "1":
        number = random.randint(1, 10)
        attempts = 3

        print("\nУ тебе 3 спроби 🎯")

        while attempts > 0:
            guess = int(input("Вгадай число (1–10): "))

            if guess == number:
                print("Правильно! 🎉")
                break
            else:
                attempts -= 1
                print("Ні 😅 Залишилось спроб:", attempts)

                if guess < number:
                    print("⬆️ Більше")
                else:
                    print("⬇️ Менше")

        if attempts == 0:
            print("Програв ❌ Число було:", number)

    elif choice == "2":
        print("Покa 👋")
        break

    else:
        print("Невірний вибір")
