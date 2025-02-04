# 1.Виправ помилку у порівнянні 3 ! 5, нічого не видаляй

print(3 != 5)

# 2.Наведи усі комбінації арифметичних порівнянь для 5 _ 5, при яких результат буде True

print(5 == 5)
print(5 >= 5)
print(5 <= 5)

# 3.Наведи 5 комбінацій з логічних операторів (or, and, not) та дужок, так щоб результат виразу True _ True _ False був True

print(True and True or False)
print(True or True or False)
print(True or True and False)
print(not(True and True and False))
print(True or  True or not(False))

# 4.Отримай логічні значення для пари аргументів (bool()) та порівняй (==) їх між собою. З'ясуй чому результат саме такий

# 1) None, 7
print(bool(None) == bool(7))
# 2)Пуста строка, вираз 10 - 1
print(bool("") == bool(10 - 1))
# 3)True or False, результат роботи функції print() з будь-яким текстом
print(bool(True or False) == bool(print("hello world")))
# 4)Результат роботи функції type() від None, результат функції id() від None
print(bool(type(None)) == bool(id(None)))
