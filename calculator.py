# This is a simple calculater program to add, subtract, multiply or divide numbers. 
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
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
# Take input from the user
    choice = input("Enter choice:")
# Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
