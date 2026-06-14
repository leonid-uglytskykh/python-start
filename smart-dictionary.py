import tkinter as tk
import json
import os

FILE_NAME = "dictionary.json"

default_words = {
    "cat": "кіт",
    "dog": "собака",
    "house": "будинок",
    "apple": "яблуко",
    "water": "вода",
    "computer": "комп'ютер",
    "school": "школа",
    "book": "книга",
    "car": "автомобіль",
    "phone": "телефон"
}

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        words = json.load(file)
else:
    words = default_words

def save_words():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(words, file, ensure_ascii=False, indent=4)

def translate():
    word = english_entry.get().lower()

    if word in words:
        result_label.config(text=words[word])
    else:
        result_label.config(text="Немає в словнику")

def add_word():
    english = english_entry.get().lower()
    ukrainian = ukrainian_entry.get().lower()

    if english and ukrainian:
        words[english] = ukrainian
        save_words()
        result_label.config(text="Слово додано")
        update_list()

def update_list():
    word_list.delete(0, tk.END)

    for english, ukrainian in sorted(words.items()):
        word_list.insert(tk.END, f"{english} -> {ukrainian}")

window = tk.Tk()
window.title("Dictionary Pro")
window.geometry("700x500")

title = tk.Label(window, text="Dictionary Pro", font=("Arial", 20))
title.pack(pady=10)

tk.Label(window, text="English word").pack()

english_entry = tk.Entry(window, width=40)
english_entry.pack()

tk.Label(window, text="Ukrainian translation").pack()

ukrainian_entry = tk.Entry(window, width=40)
ukrainian_entry.pack()

translate_button = tk.Button(
    window,
    text="Translate",
    command=translate
)
translate_button.pack(pady=5)

add_button = tk.Button(
    window,
    text="Add word",
    command=add_word
)
add_button.pack(pady=5)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.pack(pady=10)

word_list = tk.Listbox(
    window,
    width=60,
    height=15
)
word_list.pack(pady=10)

update_list()

window.mainloop()
