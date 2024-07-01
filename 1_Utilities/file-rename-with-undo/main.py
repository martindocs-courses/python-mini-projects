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
from pathlib import Path
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from InquirerPy.base.control import Choice

from rename import rename_files, rename_undo

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

  # Directory where the script resides.
  # default_path = Path(__file__).resolve().parent

  # Home path
  home_path = Path.home()
  

  if action == "Rename Files":
    rename_action = inquirer.filepath(
      message = "Enter the directory containing files to rename:",
      default = str(home_path),
      validate = PathValidator(is_dir=True, message="Input is not a directory"),
      only_directories =  True,
    ).execute()

    prefix_action = inquirer.text(
      message = "Enter the prefix to add to file names: ",
      validate = lambda txt : len(txt) > 0,
      invalid_message = "Prefix cannot be empty" 
    ).execute()
        
    rename_files(rename_action, prefix_action)

  elif action == "List Logs":
    pass

  elif action == "Undo Rename":
    pass
   

if __name__ == "__main__": main()


