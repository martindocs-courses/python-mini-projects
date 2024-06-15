
'''
  1) user input options
  - password length
  - lower case
  - upper case
  - numeric values
  - special characters

  * minimum length of the password is 8 and max 128
  * if user press enter without typing length of the pass, choose min length 8
  * if user wont choose any option, tell the user to choose at least one option

  2) show to user password strength with stars from 1 to 5
  3) give option to copy password to clipboard  

'''

import random


special_characters = [
  '@',
  '%',
  '+',
  '\\',
  '/',
  "'",
  '!',
  '#',
  '$',
  '^',
  '?',
  ':',
  ',',
  ')',
  '(',
  '}',
  '{',
  ']',
  '[',
  '~',
  '-',
  '_',
  '.'
]

numeric_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_characters = [
  'a',
  'b',
  'c',
  'd',
  'e',
  'f',
  'g',
  'h',
  'i',
  'j',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'w',
  'x',
  'y',
  'z'
]

upper_characters = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z'
]


def confirm_input(prompt):
  while True:
    user_input = input(prompt)

    if not user_input.lower() in ['y', 'n']:
      print("\nPlease confirm [Y] Yes or [N] No\n")  
    elif user_input.lower() == 'y':
      return True
    else:
      return False

def password_strength(password):
  pass




# Generate random password based on user input
def password_generator():    
  charTypes = []

  while True:

    password_length = input("Enter password length between [8 - 128] characters: ")
    confirm_lower_case = confirm_input("Confirm to include lower case letters [Y] Yes, [N] No: ")
    confirm_upper_case = confirm_input("Confirm to include upper case letters [Y] Yes, [N] No: ")
    confirm_numeric_values = confirm_input("Confirm to include numeric characters [Y] Yes, [N] No: ")
    confirm_special_characters = confirm_input("Confirm to include special characters [Y] Yes, [N] No: ")

    if confirm_lower_case and confirm_upper_case and confirm_numeric_values and confirm_special_characters == 'n':
      print("Ensure that at least one character character type is specified")    
      return password_generator()

    if confirm_lower_case:
      charTypes += lower_characters
    if confirm_upper_case:
      charTypes += upper_characters
    if confirm_numeric_values:
      charTypes += numeric_characters
    if confirm_special_characters:
      charTypes += special_characters
    

    return_values = random.choices(charTypes, k=int(password_length))
    print(return_values)

password_generator()