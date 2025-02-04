# Створи послідовність інструкцій, яка:

# 1.Отримує від користувача ім'я, де кожна літера може буте як маленького так і великого регістру, також можливі пробіли перед та після імені, наприклад  wiLLiAm   

name_user = input("Hello user, write here your name and push ENTER: ")
print(name_user)

# 2.Очищує ім'я від знаків пробілу спочатку та наприкінці (знайти метод для рядків, який це робить)

if name_user.startswith(" ") and name_user.endswith(" "):
    name_user = name_user[1:len(name_user) - 1]

# 3.Друкує привітання для цього імені у форматі перша літера велика, інші маленькі

print(name_user.capitalize())

# 4.Друкує кількість літер у імені

print(len(name_user))

# 5.Друкує ім'я задом наперед

print(name_user[::-1])
