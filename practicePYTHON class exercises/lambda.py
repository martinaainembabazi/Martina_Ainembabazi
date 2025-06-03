#Lamda functions
#used for small fynstions
numbers = [1, 2, 3, 4, 5]
squared=list(map(lambda x: x*x, numbers))
print(squared)





#assignment find the factorial of a number(five)

def factorial(n):
    return n*n-1
while True:
    try:
        n = int(input("Enter a positive integer (or 0 to exit): "))
        if n == 0:
            break
        elif n > 0:
            result = factorial(n)
            print(f"Factorial of {n} is {result}")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")



