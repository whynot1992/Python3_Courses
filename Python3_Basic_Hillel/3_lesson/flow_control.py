# We get the first value and figure it out

try:
    first_value = input("Write here your first number: ")
    
    if first_value.isdigit():
        first_value = int(first_value)
    else:
        try:
            first_value = float(first_value) if bool(float(first_value)) else first_value
        except ValueError:
            raise ValueError("Input is neither an integer or a valid float.")
except ValueError as e:
    print(f"Error: {e}")

# We get the second value and figure it out

try:
    second_value = input("Write here your first number: ")
    
    if second_value.isdigit():
        second_value = int(second_value)
    else:
        try:
            second_value = float(second_value) if bool(float(first_value)) else second_value
        except ValueError:
            raise ValueError("Input is neither an integer or a valid float.")
except ValueError as e:
    print(f"Error: {e}")

# We get operants and make action

action = input("Enter a sign from the list +, -, *, /:")

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