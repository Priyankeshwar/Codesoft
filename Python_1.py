# Creating a simple calculator:

# Adding two numbers
def addition(num_1, num_2):
    return num_1 + num_2

# Subtracting two numbers:


def subtract(num_1, num_2):
    return num_1 - num_2

# Multiply two numbers:


def multiply(num_1, num_2):
    return num_1 * num_2

# Division of two numbers:


def division(num_1, num_2):
    return num_1 / num_2


print("Select an operation :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")
print()

while True:
    input_num = int(input("Enter your choice (1/2/3/4): "))

    if input_num in (1, 2, 3, 4):
        num_1 = int(input("Enter the First Number: "))
        num_2 = int(input("Enter the Second Number: "))

        if input_num == 1:
            print(f"{num_1} + {num_2} = {addition(num_1, num_2)}")
        elif input_num == 2:
            print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
        elif input_num == 3:
            print(f"{num_1} x {num_2} = {multiply(num_1, num_2)}")
        elif input_num == 4:
            if num_2 == 0:  # To avoid the zero division error
                print("Cannot divide by zero, please enter a valid input")
            else:
                print(f"{num_1} / {num_2} = {division(num_1, num_2)}")
        break
    else:
        print("Invalid Option")
