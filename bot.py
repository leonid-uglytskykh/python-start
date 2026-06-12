while True:
    word = input("Введи англійське слово: ").lower()

    if word == "hello":
        print("Привіт")
    elif word == "cat":
        print("Кіт")
    elif word == "dog":
        print("Собака")
    elif word == "exit":
        break
    else:
        print("Не знаю цього слова")
