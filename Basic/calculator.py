import sys
from enum import Enum 

# Set of symbolic names bound to unique values
class OPERANDS(Enum):
  ADDITION = "+"
  SUBSTRACTION = "-"
  MULTIPLICATION = "*"
  DIVISION = "/"
  MODULO = "%"
  EXPONENTIATION = "**"

# Function to clear the screen
'''
  end="" - not append a newline character at the end of the output, by default it does
  flush=True - ensures that the screen clear command is executed right away
'''
clear = lambda : print("\033c", end="", flush=True)

# Function to calculate two values
def calculation(operand):
  num1 = input("\nEnter the first value: ")
  num2 = input("Enter the second value: ")  

  '''
    The isdigit() returns True only if all characters in the string are digits else returns false if any alphabet or any special character exists in the string.
  '''
  if not num1.isdigit() or not num2.isdigit():
    print("\nBoth values need to be numbers\n")
    return calculation(operand)

  result = 0
  # Switch in Python, no need for break
  match operand:
    case "+":
      result = int(num1) + int(num2)      
    case "-":
      result = int(num1) - int(num2)      
    case "*":
      result = int(num1) * int(num2)      
    case "/":
      result = int(num1) / int(num2)      
    case "%":
      result = int(num1) % int(num2)      
    case "**":
      result = int(num1) ** int(num2)      
    
  print(f"{num1} {operand} {num2} = {result}\n")

  while True:  
    play_again = input(f"Do you want to continue {OPERANDS(operand).name}?\n[Y] Yes\n[N] No\n")

    if play_again.lower() not in ["y", "n"]:
      continue 
    else:
      break
  
  if play_again.lower() == "y":
    return calculation(operand)
  else:    
      clear() # clear the screen
      return # return to the main screen, parent function, which is calculator()


# Main function calculates two values
def calculator(): 
  while True:  
    operation = input("***Calculator options***\n[+] Additions\n[-] Substraction\n[*] Multiplication\n[/] Division\n[%] Modulo\n[**]Exponentiation\n\n[x] to exit\n\n")

    if operation not in ['+', '-', '*', '/', '%', '**', 'x']:
      print("\nYou must provide a valid operand\n")
      return calculator()    

    if operation == '+':
      calculation("+")
    elif operation == '-':
      calculation("-")      
    elif operation == '*':
      calculation("*")            
    elif operation == '/':
      calculation("/")                  
    elif operation == '%':
      calculation("%")                        
    elif operation == '**':
      calculation("**")                        
    else:
      sys.exit("Bye! 👋")

calculator()