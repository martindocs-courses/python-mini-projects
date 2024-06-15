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

def show_log(log):

  if not log: # logical negation   
    print("*** Session log empty ***\n")   
  else:    
    print("*** Session log ***")
    for entry in log:
      print(f" {entry}")
    print("*******************\n")

# Main function Calculator
def calculator(): 
  session_log = []

  # Function to calculate two values
  def calculation(operand):
    nonlocal session_log
    
    # check if the value is digit
    def check_digit(prompt):       
      while True:
        num = input(prompt)
        '''
          The isdigit() returns True only if all characters in the string are digits else returns false if any alphabet or any special character exists in the string.
        '''
        if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
          return int(num)
        else:
          print("Invalid input. Please provide a valid integer.")
   
    num1 = check_digit("\nEnter the first value: ")
    num2 = check_digit("Enter the second value: ")

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
        try:
          result = int(num1) / int(num2)              
        except ZeroDivisionError: 
          print("Cannot divide by zero!")
      case "%":
        result = int(num1) % int(num2)      
      case "**":
        result = int(num1) ** int(num2)      
      
    log_entry = f"{num1} {operand} {num2} = {result}"
    session_log.append(log_entry)

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
        return # return to the main screen, parent function calculator()


  while True:  
    operation = input("***Calculator options***\n[+] Additions\n[-] Substraction\n[*] Multiplication\n[/] Division\n[%] Modulo\n[**]Exponentiation\n\n[l]Show session log\n[x]to exit\n\n")

    if operation.lower() not in ['+', '-', '*', '/', '%', '**', 'l', 'x']:
      print("\nYou must provide a valid operand\n")
      return calculator()    
   
    if operation == 'x':
      sys.exit("Bye! 👋")
    elif operation == 'l':
      show_log(session_log)
    else: 
      calculation(operation)


calculator()