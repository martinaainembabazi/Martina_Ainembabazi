#Syntax errors
#Logic errors
#Runtime errors
  


try:
    result=10/0
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')

    else:
    print('Successful',result)
    finally:
    print('Execution completed')

    #Raise a custom exception that checks a positive number
    x = -1

if x < 0:
  raise Exception("Negative number error: x must be positive")