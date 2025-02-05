def checking_value(row_value):
    try:
        if bool(float(row_value)) or row_value.isdigit():
            return print("All OK")
    except ValueError:
        return print("You made a mistake in the water, a real or integer number " \
              "should be written here")
         
        

def main():
    first_value = checking_value(input("Write here your first number: "))
    # second_value = checking_value(input("Write here your second number: "))
    # return print(first_value + second_value)
    return first_value

if __name__ == "__main__":
    main()
