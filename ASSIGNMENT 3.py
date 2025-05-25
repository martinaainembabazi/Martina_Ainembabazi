def get_number(n):
    return float(input(f"Enter the number {n}: "))

while True:
    try:
        x = get_number("x")
        y = get_number("y")
        answer = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero value for y.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    else:
        print(f"The result of {x} divided by {y} is {answer}.")
        break