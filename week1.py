
   # a simple calculator program that performs addition, subtraction,
# multiplication, and division based on user input.

def calculator():
    """
    Asks the user for two numbers and an operation, then performs
    the calculation and prints the result.
    """
    print(" Basic Calculator!")

    try:
        
        num1 = float(input("Enter the first number: "))
        
        
        num2 = float(input("Enter the second number: "))
        
        
        operator = input("Enter an operator (+, -, *, /): ")

        result = 0
        
        # Check the operator and perform the corresponding calculation.
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero to prevent an error.
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return # Exit the function if division by zero occurs.
            result = num1 / num2
        else:
            print("Error: Invalid operator.")
            return # Exit the function if the operator is not valid.

        # Print the formatted result.
        print(f"{num1} {operator} {num2} = {result}")
        
    except ValueError:
        # Catch non-numeric input.
        print("Error: Invalid input. Please enter numbers only.")

calculator()