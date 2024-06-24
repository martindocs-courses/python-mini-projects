"""
Description: Count the number of words in a given text.

Steps:
1 - ask for the path to the file/text or load the current path where script is located
2 - analise the text
3 - show the results in the console

Concepts: Strings, loops, file I/O.

"""

from pathlib import Path


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


def main():
  target_dir = get_target_folder()

 



if __name__ == "__main__": main()