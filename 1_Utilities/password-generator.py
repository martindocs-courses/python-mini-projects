import random
import re

special_characters = [
  '!',
  '@',
  '#',
  '$',
  '%',
  '^',
  '&',
  '*',
  '(',
  ')',
  ',',
  '.',
  '?',
  '"',
  ':',
  '{',
  '}',
  '\'',
  '|',
  '<',
  '>'
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


# Checks user confirmation input
def confirm_input(prompt):
  while True:
    user_input = input(prompt)

    if user_input.lower() not in ['y', 'n']:
      print("\nPlease confirm [Y] Yes or [N] No\n")  
    elif user_input.lower() == 'y':
      return True
    else:
      return False


# Clear the screen
clear_screen = lambda : print("\033c", end="", flush=True)


# Determinate password strength, based on user character choices and length of the password
def password_strength(password):
  # criteria, where:
  '''
    * 'r' means raw string and ensure that any backslashes in the regex pattern are treated literally
    * re.search() - searches the string for the first occurrence of the pattern and returns a match object if found, or None if not found.  
  '''

  has_length = len(password)  
  has_lower_char = bool(re.search(r'[a-z]', password))
  has_upper_char = bool(re.search(r'[A-Z]', password))
  has_numeric_char = bool(re.search(r'\d', password))
  has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)) 
  
  all_criteria = [has_lower_char, has_upper_char, has_numeric_char, has_special_char]

  # Sum all character choices
  score = sum(all_criteria)

  # Check the password strength first based on the password length and then the chosen character
  if has_length <= 11:
    if score == 4:
      strength = "Strong"
    elif score == 3:
      strength = "Moderate"
    else:
      strength = "Weak"

  if has_length > 11 and has_length <= 19:
    if score >= 3:
      strength = "Strong"
    elif score == 2:
      strength = "Moderate"
    else:
      strength = "Weak"
  
  if has_length > 19 and has_length <= 39:
    if score >= 2:
      strength = "Strong"    
    else:
      strength = "Moderate"
  
  if has_length > 39 and has_length <= 79:
    if score >= 2:
      strength = "Very Strong"    
    else:
      strength = "Strong"

  if has_length > 79 and has_length <= 128:
    if score >= 2:
      strength = "Extremely Strong"    
    else:
      strength = "Very Strong"

  return strength


# Generate the random password 
def password_generator():    

  confirm_password_length = input("Enter password length between [8 - 128] characters: ")

  # If user press Enter, set default value to 8
  if not confirm_password_length:
    confirm_password_length = "8"

  # Check if password langth is within the allowed range and if it's a digit
  if not confirm_password_length.isdigit() or int(confirm_password_length) < 8 or int(confirm_password_length) > 128:
    print("\nEnsure that at value is correct!!\n")    
    return password_generator()
  
  confirm_lower_case = confirm_input("Confirm to include lower case letters (y/n): ")
  confirm_upper_case = confirm_input("Confirm to include upper case letters (y/n): ")
  confirm_numeric_values = confirm_input("Confirm to include numeric characters (y/n): ")
  confirm_special_characters = confirm_input("Confirm to include special characters (y/n): ")

  # Prompt user to choose at least one character type
  if not confirm_lower_case and not confirm_upper_case and not confirm_numeric_values and not confirm_special_characters:
    print("Ensure that at least one character character type is specified!!")    
    return password_generator()
  
  charTypes = [] # list of all chosen character types
  password = [] 

  # Get one character from each character type user selection
  # Also add chosen character type to the list of characters types
  if confirm_lower_case:  
    charTypes += lower_characters
    password += random.choices(lower_characters)
  if confirm_upper_case:
    charTypes += upper_characters
    password += random.choices(upper_characters)
  if confirm_numeric_values:
    charTypes += numeric_characters
    password += random.choices(numeric_characters)
  if confirm_special_characters:
    charTypes += special_characters
    password += random.choices(special_characters)
    
  # Get the remaning password length
  remaning_password = int(confirm_password_length) - len(password)

  # Generate remaning random characters and add to the password
  password += random.choices(charTypes, k=remaning_password)

  random.shuffle(password)

  output = ''.join(password)

  print(f"\nGenerated password: {output}")
  print(f"Password strenght: {password_strength(output)} \n")

  # Ask user if he/she wants to get a new password
  while True:
    generate_password_again = input("Do you want to generate a new password? (y/n): ")

    if generate_password_again not in ['y', 'n']:
      continue
    else:
      print("Bye! 👋")
      break
  
  if generate_password_again.lower() == "y":
    clear_screen()
    return password_generator()  

password_generator()