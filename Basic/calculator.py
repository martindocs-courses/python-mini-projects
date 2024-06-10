import sys

def add():
  value1 = input("Enter the first value")
  value2 = input("Enter the second value")  

def subtract(num1, num2):
  pass

def divide(num1, num2):
  pass

def multiply(num1, num2):
  pass

def modulo(num1, num2):
  pass


def calculator():
  options = True

  while options:  
    operation = input("***Choose your option***\n[+] Additions\n[-] Substraction\n[*] Multiplication\n[/] Division\n[%] Modulo\n\n[x] to exit the Calculator")

    if operation not in ['+', '-', '*', '/', '%']:
      print("\nYou must provide a valid operation\n")
      return calculator()    

    if operation == '+':
      add()
    elif operation == '-':
      pass
    elif operation == '*':
      pass
    elif operation == '/':
      pass
    elif operation == '%':
      pass
    else:
      sys.exit()

if __name__ == "__main__":
  calculator()

'''
  - user choosing operation, addition, subtraction, multiplication form the list etc.
  - user input values and check for validity
  - return opartin value

'''