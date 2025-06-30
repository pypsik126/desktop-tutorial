print("Це гра квіз на мільйон")
print("Буде 10 питань")

score = 0

print("\nПитання 1:")
cat = input("Яка найбільша область України? ")
if cat.lower() == "одеська":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 2:")
kot = input("Яке традиційне вбрання українців? ")
if kot.lower() == "вишиванка":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 3:")
lom = input("Яке море омиває Україну з Одесою? ")
if lom.lower() == "чорне море" or lom.lower() == "чорне":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 4:")
pol = input("У якому році Україна отримала незалежність? ")
if pol == "1991":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 5:")
question5 = input("Хто є автором українського гімну (слова)? ")
if question5.lower() == "павло чубинський" or question5.lower() == "чубинський":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 6:")
question6 = input("Як називалася козацька держава на території України? ")
if question6.lower() == "гетьманщина":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 7:")
question7 = input("У якому столітті відбулося хрещення Русі? ")
if question7 == "10" or question7.lower() == "x":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 8:")
question8 = input("Назвіть прізвище гетьмана, який очолив національно-визвольну війну середини XVII століття. ")
if question8.lower() == "хмельницький" or question8.lower() == "богдан хмельницький":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 9:")
question9 = input("Яке місто було столицею Київської Русі? ")
if question9.lower() == "київ":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\nПитання 10:")
question10 = input("Як називається основний закон України? ")
if question10.lower() == "конституція" or question10.lower() == "конституція україни":
    print("Молодець")
    score += 1
else:
    print("ВИЙДИ З ТЕСТУ")

print("\n---")
print(f"Тест завершено! Ваш результат: {score} правильних відповідей з 10.")
print("---")