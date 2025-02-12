# 1. Створи функцію, яка приймає параметри start та end, підсумовує всі цілі числа від значення start 
#     до величини end включно. Якщо користувач задасть перше число більше, ніж друге, поміняй їх місцями

def sum_number(start, end):

    if start > end:
        start, end = end, start

    return sum(list(range(start, end + 1)))


answer = sum_number(10, 1)
print(answer)


# 2. Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди. Функція може прийняти
#     число як рядок так і як ціле число.

def day_hour_min_sec(value):

    days = value // (24 * 3600)
    remaining_sec = value % (24 * 3600)

    hours = remaining_sec // 3600
    remaining_sec %= 3600

    minutes = remaining_sec // 60

    secundes = remaining_sec % 60

    return print(f"{days}:{hours}:{minutes}:{secundes}")

day_hour_min_sec(987654)


# 3. Створи три функції, які обчислюють суму чисел у списку:
#       - з for-циклом
#       - з while-циклом
#       - з рекурсією

def sum_for(any_list):
    countere = 0

    for i in any_list:
        countere += int(i)

    return countere

def sum_while(any_list):
    counter = 0
    answer = 0

    while counter < len(any_list):
        answer += any_list[counter]
        counter += 1

    return answer

def sum_rec(any_list):

    if not any_list:
        return 0
    return any_list[0] + sum_rec(any_list[1:])


listik = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum_for(listik))
print(sum_while(listik))
print(sum_rec(listik))


# 4. Створи функцію яка обчислює числа Фібоначчі. Функція повертає число з послідовності за порядковим номером

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=" ")

# 5. Надрукуй 4 рядки: помідор -> м'ясо -> сир -> хліб, умови:
#       1) Створи 4 функції, кожна друкує свій шар
#       2) Викликай лише одну функцію
#       3) Використай синтаксис декораторів
#       4) Очікуваний результат друку:
#            - помідор
#            - м'ясо
#            - сир
#            - хліб

def tomato_layer(func):
    def wrapper():
        print("помідор")
        func()
    return wrapper

def meat_layer(func):
    def wrapper():
        print("м'ясо")
        func()
    return wrapper

def cheese_layer(func):
    def wrapper():
        print("сир")
        func()
    return wrapper

def bread_layer(func):
    def wrapper():
        print("хліб")
    return wrapper

@tomato_layer
@meat_layer
@cheese_layer
@bread_layer
def sandwich():
    pass

sandwich()
