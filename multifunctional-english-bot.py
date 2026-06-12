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

def chatbot():
    while True:
        message = input("Ти: ").lower()

        if message == "привіт":
            print("Бот: Привіт")
        elif message == "як справи":
            print("Бот: Добре")
        elif message == "хто ти":
            print("Бот: Я English Bot")
        elif message == "вихід":
            break
        else:
            print("Бот: Не розумію")

def quiz():
    global score

    for english, ukrainian in words.items():
        answer = input(f"Переклади '{english}': ").lower()

        if answer == ukrainian:
            print("Правильно")
            score += 1
        else:
            print("Неправильно")
            print("Правильна відповідь:", ukrainian)

while True:
    print()
    print("1 - Перекладач")
    print("2 - Вікторина")
    print("3 - Чат-бот")
    print("4 - Показати словник")
    print("5 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        word = input("Слово: ").lower()

        if word in words:
            print(words[word])
        else:
            print("Немає в словнику")

    elif choice == "2":
        quiz()

    elif choice == "3":
        chatbot()

    elif choice == "4":
        for english, ukrainian in words.items():
            print(english, "->", ukrainian)

    elif choice == "5":
        break

print("Підсумковий score:", score)
