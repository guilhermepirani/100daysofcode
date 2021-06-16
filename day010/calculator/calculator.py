'''Command line calculator'''

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    num1 = int(input("What's the first number? "))
    should_continue = True

    while should_continue:
        operation_symbol = input(f"Pick an operation {[x for x in operations]}: ")
        num2 = int(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        while True:
            more_ops = input(f'Type "y" to continue calculating with {answer} or "n" to begin a new calculation.: ').lower()

            if more_ops == 'y':
                num1 = answer
                break
            elif more_ops == 'n':
                should_continue = False
                calculator()

if __name__ == '__main__':
    print(logo)
    calculator()