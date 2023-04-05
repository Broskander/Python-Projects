def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    user_input = int(input())
    first = int(input("Please select your first number: "))
    second = int(input("Please select your second number: "))

    if (user_input == 1):
        print(first, " + ", second, " = ", add(first, second))

    elif (user_input == 2):
        print(first, " - ", second, " = ", subtract(first, second))

    elif (user_input == 3):
        print(first, " * ", second, " = ", multiply(first, second))

    elif (user_input == 4):
        print(first, " / ", second, " = ", divide(first, second))

    else:
        print("Invalid input.")


print(
    "Welcome to the calculator program. Select 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division.")

main()

while True:
    rerun = int(input("\nWould you like to run again? (1 for yes, 2 or No)\n"))
    if rerun == 2:
        break
    if rerun == 1:
        print("\nSelect 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division.")
        main()
