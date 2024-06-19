'''
Desc: Create a script that organizes your image files into folders by the date they were taken, extracting the date from the file metadata.

* User Input for Directory Selection: 
  - Prompt the user to input the path of the directory containing the images or give default path when press enter
  - Ask for for path where to move the files or set default as where image are located
  - Before starting the organization process, ask the user to confirm the action (e.g., "Do you want to organize the images in the directory 'path/to/directory'? (yes/no)").
* Display Progress: As you process each image, display the progress in the terminal (e.g., "Processing image 1 of 100...").
* Error Handling: Handle common errors and inform the user (e.g., "Error: No images found in the specified directory").

Libs:
Pillow, os, shutil

'''

from pathlib import Path
from PIL import Image
import os

def get_images_directory():
  # get the default user home directory and add path the 'Picture' folder to it
  os_home_directory = Path.home() / 'dev/_Pictures' # TEMP folder for development on WSL

  # or ask user to specify the directory
  user_directory = input("Enter full path to the images directory or press ENTER for default home directory (/home/user/Pictures): ")
  
  is_path_exist = Path(user_directory).exists()

  if user_directory and is_path_exist:
    return user_directory

  if not is_path_exist:
    print("Please enter a existing directory.")
    return get_images_directory()

  return os_home_directory


def get_directory():
  pass

def organize_files(directory):
  pass

def error_handler():
  pass
 
def extract_image_data(image):
  pass

def create_folders(name):
  pass

def main():
 pass

 
  


main()