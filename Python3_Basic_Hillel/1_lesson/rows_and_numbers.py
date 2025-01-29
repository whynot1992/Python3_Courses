# 1. Створи послідовність інструкцій, яка:

#   1) Отримує від користувача його ім'я, виводить на друк привітання для цього імені, використовуючи f-string

user_name = input("Write here your name and push ENTER: ")
print(f"Hello {user_name}, glad to see you!!!")

#   2) Отримує від користувача дрібне число, виводить на друк:

fractional_number = float(input("Write here your number and push ENTER: "))

#       1 - Отримане число

print(fractional_number)

#       2 - Ціле число (число без дрібної частини)

print(int(fractional_number))

#       3 - 4ту ступінь цілого числа

print(int(fractional_number) ** 4)

#       4 - Корінь цілого числа

print(int(fractional_number) ** 0.5)

#       5 - Залишок від ділення цілого числа на 2

print(int(fractional_number) % 2)
