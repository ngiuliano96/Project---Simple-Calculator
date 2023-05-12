# Calculator Program
from replit import clear
from art import logo

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    clear()

    # Greet user
    print(logo)
    print("Welcome to the simple calculator!")
    
    # Gather necessary user inputs
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    
    calculating = True
    while calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        result = round(calculation(num1, num2), 2)
       
        print(f"{num1} {operation_symbol} {num2} = {result}")
    
        # Allow for a user defined number of chain calculations
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            calculating = False
            calculator()

calculator()