# 1.Відтвори ASCII таблицю у вигляді словника, обов'язкові умови:
#       - Використай генератор словника
#       - Використай вбудовану функцію chr()

ascii_table = {i: chr(i) for i in range(128)}

print(ascii_table)

# 2.Реалізувати послідовність операцій яка
#       - Приймає від користувача строку тільки з літер, без пробілів
#       - Приймає від користувача пароль у вигляді цілого числа
#       - Створює словник шифра метода одноалфавітної підстановки на базі пароля. Тобто пароль - число 
#                на яке треба збільшити порядковий номер літери у алфавіті
#       - Шифрує строку на базі словника шифра. Приклад
#               + Звичайний порядок "a" - 1, "b" - 2, ..., "z" - 26 -> словник "a"="a", "b"="b", ..., "z"="z"
#               + З паролем у 4 порядок стає "a" - 5, "b" - 6, ..., "z" - 4 -> словник "a"="e", "b"="f", ..., "z"="d"
#               + Рядок "hello" перетворюється на "lipps"
#       - Друкує зашифровану строку

import sys


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_dict = {letter: index for index, letter in enumerate(alphabet, start=1)}
reversed_alphabet = {v: k for k, v in alphabet_dict.items()}

user_text = input("Write here your text: ").lower()

if user_text.isalpha():
    user_password = input("Write here your Integer number: ")

    try:
        row_output = list()

        if int(user_password):

            for char in user_text:
                new_index = (alphabet_dict[char] + int(user_password) - 1) % 26 + 1
                row_output.append(reversed_alphabet[new_index])

        output = ''.join(row_output)
        print(output)

    except ValueError as error:
        print(f"Your number is not a whole number.")

else:
    print("Just enter text consisting of letters. Numbers and signs, as well as spaces, are not accepted")
    sys.exit()
