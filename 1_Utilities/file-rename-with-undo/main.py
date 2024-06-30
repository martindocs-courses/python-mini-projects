"""
Description: Rename multiple files in a directory based on specified patterns, with an option to undo the renaming operation.

Steps:
1 - display interactive command-line prompts, using InquirerPy lib
2 - load/save logs from/to *.json file
3 - rename files in a specified directory
4 - list logs based on timestamp from *.json file
5 - undo renamed files

Concepts: file I/O, data structures, error handling, libs
"""
import os
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from InquirerPy.base.control import Choice

def main():

  action = inquirer.rawlist(
    message = "What would you like to do?",
    choices = [
      "Rename Files", 
      "List Logs", 
      "Undo Rename", 
      Choice(value = None, name = "Exit")
    ],
    default = 1
  ).execute()

  # Defult root directory for Unix and Windows systems
  home_path = "~/" if os.name == "posix" else "C:\\"

  if action == "Rename Files":
    rename_action = inquirer.filepath(
      message = "Enter the directory containing files to rename:",
      default = home_path,
      validate = PathValidator(is_dir=True, message="Input is not a directory"),
      only_directories =  True,
    ).execute()

    prefix_action = inquirer.text(
      message = "Enter the prefix to add to file names: ",
      validate = lambda txt : len(txt) > 0,
      invalid_message = "Prefix cannot be empty" 
    ).execute()

    # pass values: rename_action and prefix_action to Reanme method

 

if __name__ == "__main__": main()


