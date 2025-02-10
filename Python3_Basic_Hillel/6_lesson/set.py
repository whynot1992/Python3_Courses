# 1.Створити послідовність інструкцій, яка друкує результат аналізу 2 наборів текстових даних з будь-яких символів,
#   отриманих від користувача
#       - Список літер, які присутні в обох наборах, регістр має значення ("A" та "a" - окремі літери). Літери не повторювати
#       - Список цифр, які є в першому або в другому наборі, але не в обох. Цифри не повторювати

first_input = input("Writer here your first text: ")
second_input = input("Writer here your second text: ")

ended_input = set(first_input).union(set(second_input))
print(f"Your typing has similar characters like this: {list(ended_input)}")


ended_set = {el for el in set(first_input).symmetric_difference(set(second_input)) if el.isdigit()}

print(f"A list of numbers, some in the first or the other set, 
      but not both. Don't repeat the numbers: {list(ended_set)}")


# 2.Знайди та ознайомся з операторами |=, &=, -=, ^=, та методами які відповідають цим операторам. Наведи по 
#   1 прикладу для кожного оператора, використовуй 3 множини одночасно у якості операндів 

a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}

# Об'єднання множин
a |= b | c
print(a)

# Перетин множин
a &= b & c
print(a)

# Різниця множин
a -= b | c
print(a)

# Симетрична різниця множин
a ^= b ^ c
print(a)


