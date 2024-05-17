from replit import clear
from calcualtor_logo import logo


# Adding
def add(number1, number2):
    return number1 + number2


# Subtracting
def subtract(number1, number2):
    return number1 - number2


# Multiplying
def multiply(number1, number2):
    return number1 * number2


# Dividing
def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number: "))
    for operation in operations:
        print(f"{operation}")
    stop_calc = True
    while stop_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {round(answer, 1)}")
        continue_calc = input(f"Type 'y' to continue with {round(answer, 1)}, or type 'n' to start new calculation.: ").lower()
        if continue_calc == 'n':
            stop_calc = False
            clear()
            calculator()
        elif continue_calc == 'y':
            num1 = round(answer, 1)
        else:
            print("Good bye have a nice day!")
            stop_calc = False


calculator()
