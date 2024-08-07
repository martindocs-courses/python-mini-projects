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
from logs import list_logs, load_logs

def main():

  # main menu
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

  # Home path directory
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
    logs = list_logs()

    if logs:
      for log in logs:
        print(log)   

  elif action == "Undo Rename":
    logs = load_logs()

    if logs:
      log_chices = logs.keys()

      undo_choices = inquirer.rawlist(
        message = "Select the timestamp of the rename operation to undo:",
        choices = log_chices, 
        default = 1
      ).execute()
      
      rename_undo(undo_choices) 
   

if __name__ == "__main__": main()


