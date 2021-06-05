## This is a simple calculater program to add, subtract, multiply or divide numbers.
# This  adds two numbers
def add(x, y):
    return x + y
# This  subtracts two numbers
def subtract(x, y):
    return x - y
# This  multiplies two numbers
def multiply(x, y):
    return x * y
# This  divides two numbers
def divide(x, y):
    return x / y
# Player's options for input.
print("Select operation.")
print("(1) Add")
print("(2) Subtract")
print("(3) Multiply")
print("(4) Divide")
while True:
    choice = input("Enter choice:") # Take input from the user
# The players pivks which one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: ")) # Take first input integer num from the player
        num2 = int(input("Enter second number: ")) # Take second input integer num from the player

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2)) # adding num1 and Num2 together

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2)) # subtract num1 and Num2

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2)) # multiply num1 and Num2 together

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2)) # divide num1 and Num2 together
        break # end program
    else:
        print("Invalid Input")
