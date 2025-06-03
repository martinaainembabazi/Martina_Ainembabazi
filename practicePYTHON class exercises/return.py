def get_vals(x, y):
    return x / y

try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = get_vals(x, y)
    print(f"The result of {x} divided by {y} is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
