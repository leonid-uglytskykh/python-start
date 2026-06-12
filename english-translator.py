words = {
    "cat": "кіт",
    "dog": "собака",
    "house": "будинок",
    "apple": "яблуко",
    "water": "вода",
    "computer": "комп'ютер",
    "school": "школа",
    "book": "книга",
    "car": "автомобіль",
    "phone": "телефон",
    "sun": "сонце",
    "moon": "місяць",
    "friend": "друг"
}

score = 0

print("English Dictionary Bot PRO")
print("Команди: translate / add / list / exit")

while True:
    command = input("\nЩо робимо? ").lower()

    if command == "translate":
        word = input("Введи англійське слово: ").lower()

        if word in words:
            print("Переклад:", words[word])
            score += 1
        else:
            print("Немає в словнику")

            add = input("Хочеш додати це слово? (yes/no): ").lower()

            if add == "yes":
                translation = input("Переклад українською: ").lower()
                words[word] = translation
                print("Додано")

    elif command == "add":
        word = input("Англійське слово: ").lower()
        translation = input("Український переклад: ").lower()

        words[word] = translation
        print("Додано")

    elif command == "list":
        print("Словник:")
        for w, t in words.items():
            print(w, "->", t)

    elif command == "exit":
        print("До побачення")
        break

    else:
        print("Невідома команда")

print("Score:", score)
