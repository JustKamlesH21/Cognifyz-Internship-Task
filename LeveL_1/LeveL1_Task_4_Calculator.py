#Calculator Program
def add(x, y):
    print("Result:", x + y)

def subtract(x, y):
    print("Result:", x - y)

def multiply(x, y):
    print("Result:", x * y)

def divide(x, y):
    if y == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", x / y)

def modulus(x, y):
    print("Result:", x % y)

while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            add(num1, num2)
        elif choice == '2':
            subtract(num1, num2)
        elif choice == '3':
            multiply(num1, num2)
        elif choice == '4':
            divide(num1, num2)
        elif choice == '5':
            modulus(num1, num2)
    else:
        print("Invalid choice. Please select a valid option.")

