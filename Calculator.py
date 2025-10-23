num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation using if-elif statements
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    # Handle division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operator entered")
