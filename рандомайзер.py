import random

# Генеруємо випадкове число від 1 до 10
secret_number = random.randint(1, 10)

print("Вгадай число від 1 до 10!")

while True:
    try:
        guess = int(input("Введи своє число: "))

        if guess < 1 or guess > 10:
            print("Будь ласка, введи число від 1 до 10.")
            continue

        if guess == secret_number:
            print("Вітаю! Ти вгадав число!")
            break
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")
    except ValueError:
        print("Будь ласка, введи ціле число.")