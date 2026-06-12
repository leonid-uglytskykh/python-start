score = 0

def ask(word, answer):
    global score

    user = input(f"Переклади слово '{word}': ").lower()

    if user == answer:
        print(" Правильно!")
        score += 1
    else:
        print(f" Неправильно. Правильна відповідь: {answer}")

print("English Tutor Bot")

ask("cat", "кіт")
ask("dog", "собака")
ask("house", "будинок")
ask("apple", "яблуко")
ask("school", "школа")
ask("water", "вода")
ask("book", "книга")
ask("computer", "компʼютер")

print("\nРезультат:", score, "/ 8")
