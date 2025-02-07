# Створи послідовність інструкцій, у вигляді 1 циклу. Цикл працює один раз. Відповіді виводяться у рядок, 
#       у консолі буде роздруковано 3 рядки. Вимоги до кода:

# 1.Приймає від користувача рядок будь-яких символів, наприклад S f-FaGA a
# 2.Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFG
# 3.Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це  1, 8
# 4.Друкує усі гласні букви з рядка, у прикладі вище це  aAa
# 5.Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається
#     та друкується повідомлення про цю подію. Інакше друкується повідомлення про коректне завершення циклу

input_user = input("Write here your message: ")
vowel_letters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
counter = 0
all_okay_printed = False



while True:
    
    for letter in input_user:
        if letter.istitle():
            print(letter, end="")

    print("")

    for index, space in enumerate(input_user):
        if space == " ":
            print(index, end=", ")

    print("")

    for letter in input_user:
        if letter in vowel_letters:
            print(letter, end="")
    
    print("")

    for i in input_user:
        if i.isdigit():
            counter += 1
            if counter >= 3:
                print("You have 3 digits in a row")
                break
        else:
            counter = 0 

    if counter < 3 and not all_okay_printed:
        print("All okay!")
        all_okay_printed = True

    break