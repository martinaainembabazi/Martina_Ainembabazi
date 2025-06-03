class CustomException(Exception):
    pass

def positive(x):
  if x < 0:
    raise CustomException("Negative number error: x must be positive")
  return x

try:
    positive(-5)
except CustomException as e:
    print(e)
