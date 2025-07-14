# Калькулятор з 4 функціями: додавання, віднімання, множення, ділення

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль"
    return a / b

# Введення чисел
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Виклик функцій і виведення результатів
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")