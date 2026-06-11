import random

number = random.randint(1, 10)

guess = int(input("Вгадай число від 1 до 10: "))

if guess == number:
  print("Правильно!")
else:
  print("Ні, було число:", number)
