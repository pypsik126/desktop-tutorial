translator = {
    "кіт": "cat",
    "собака": "dog",
    "будинок": "house",
    "вікно": "window",
    "стіл": "table",
    "книга": "book",
    "ручка": "pen",
    "дерево": "tree",
    "машина": "car",
    "вода": "water"}
word = input("Введіть слово українською: ").lower()
if word in translator:
    print(f"Переклад: {translator[word]}")
else:
    print("Слово не знайдено у словнику.")