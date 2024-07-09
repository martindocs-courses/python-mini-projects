"""
Description: Count the number of words in a given text.

Steps:
1 - ask for the path to the file/text or load the current path where script is located
2 - analise the text
3 - show the results in the console

Concepts: Strings, loops, file I/O.

"""

from pathlib import Path
import os
import re

# Prompt user for directory or use script directory if none provided.
def get_target_folder():

  # curent working script directory
  """
    __file__  - the path of the current script file
    .resolve() - method of pathlib, which resolves the path to an absolute path
  """
  os_script_dir = Path(__file__).resolve().parent
 
  # user specified directory
  user_target_dir = input("Enter the path to the file/text or press ENTER if text is in the same directory as current main file: ")

  is_path_exist = Path(user_target_dir).exists()
 
  if user_target_dir and is_path_exist:
    return user_target_dir
  
  if not is_path_exist:
    print("Please enter a valid existing directory.")
    return get_target_folder()

  return os_script_dir


# Count and print the number of words in the file.
def word_count(file, name):
  # matches any non-word character
  words_list = re.split(r"\W+" , file.read())
  
  filter_not_words = [ word for word in words_list if not word.isdigit() and word]
  count = len(filter_not_words)
 
  print(f"\nWord count for the file '{name}': {str(count)}\n")


# Process all files in the given folder and its subdirectories for word count.
def get_file(folder):

  for(root , _ , files) in os.walk(folder, topdown=True):    
        
    non_python_files = [ file for file in files if not file.endswith(".py")]

    if non_python_files:

      for file in non_python_files:
        file_path = Path(root, file)      
        file_name = file_path.name             
          
        try:          
          current_file = open(file_path, "r")

          word_count(current_file, file_name)

        except Exception as error:
          print(f"Error reading file {file_name}: {error}")
        
        finally:
          current_file.close()

    else:
      print("\nNo files found\n")
  

def main():
  target_dir = get_target_folder()

  if target_dir:
    get_file(target_dir)


if __name__ == "__main__": main()