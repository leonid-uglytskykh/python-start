score = 0

questions = [
    ["cat", "кіт"],
    ["dog", "собака"],
    ["house", "будинок"],
    ["apple", "яблуко"],
    ["water", "вода"],
    ["computer", "компʼютер"],
    ["book", "книга"],
    ["school", "школа"]
]

for item in questions:
    answer = input(f"Переклади '{item[0]}': ").lower()

    if answer == item[1]:
        print("✅")
        score += 1
    else:
        print("❌")

print("Результат:", score)
