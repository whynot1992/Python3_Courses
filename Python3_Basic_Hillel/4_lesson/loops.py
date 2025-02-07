# 1)Cтвори послідовність інструкцій, у вигляді 1 циклу. Цикл працює один раз. Відповіді виводяться у рядок, 
#       у консолі буде роздруковано 3 рядки. Вимоги до кода:

#   1.Приймає від користувача рядок будь-яких символів, наприклад S f-FaGA a
#   2.Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFG
#   3.Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це  1, 8
#   4.Друкує усі гласні букви з рядка, у прикладі вище це  aAa
#   5.Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається
#       та друкується повідомлення про цю подію. Інакше друкується повідомлення про коректне завершення циклу

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

# 2)На базі калькулятора з практичного завдання у розділі Розгалуження, створи нескінченний 
#       цикл до доки користувач не введе exit замість будь-якого з операндів або оператора

while True:

    try:

        first_value = input("Write here your first number: ")

        if first_value == "exit" or first_value == "EXIT":
            break
        else:
            if first_value.isdigit():
                first_value = int(first_value)
            else:
                try:
                    first_value = float(first_value) if bool(float(first_value)) else first_value
                except ValueError:
                    raise ValueError("Input is neither an integer or a valid float.")
                
    except ValueError as e:
        print(f"Error: {e}")

    try:

        second_value = input("Write here your first number: ")
        if second_value == "exit" or second_value == "EXIT":
            break
        else:
            if second_value.isdigit():
                second_value = int(second_value)
            else:
                try:
                    second_value = float(second_value) if bool(float(first_value)) else second_value
                except ValueError:
                    raise ValueError("Input is neither an integer or a valid float.")
                
    except ValueError as e:
        print(f"Error: {e}")

    action = input("Enter a sign from the list +, -, *, /:")

    if action == "exit" or action == "EXIT":
        break
    else:
        if action not in ["+", "-", "*", "/"]:
            print("You make mistake! You need to type a sing from the list +, -, *, /.")
        else:
            if action == "+":
                print(f"Your answer: {first_value} {action} {second_value} = {first_value + second_value}")
            elif action == "-":
                print(f"Your answer: {first_value} {action} {second_value} = {first_value - second_value}")
            elif action == "*":
                print(f"Your answer: {first_value} {action} {second_value} = {first_value * second_value}")
            elif action == "/":
                try:
                    print(f"Your answer: {first_value} {action} {second_value} = {first_value / second_value}")
                except ZeroDivisionError:
                    print("Cannot divide by zero!")