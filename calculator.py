#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculation():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  
  continue_cal = True
  
  while continue_cal:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    new = input("Type y to continue or n to start a new calculation or x to exit ")
  
    if new == "y":
      num1 = answer
    elif new == "n":
      continue_cal = False
      calculation()
    else:
      continue_cal = False

calculation()

