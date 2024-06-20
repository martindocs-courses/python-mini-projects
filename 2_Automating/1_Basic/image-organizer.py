from pathlib import Path
from PIL import Image
import shutil
import os


def get_images_directory():
  # get the default user home directory and add path the 'Picture' folder to it
  os_home_directory = Path.home() / 'Pictures' 

  # or ask user to specify the directory
  user_directory = input("\nEnter full path to the images directory or press ENTER for default home directory (/home/user/Pictures): ")
  
  is_path_exist = Path(user_directory).exists()

  if user_directory and is_path_exist:
    return Path(user_directory)

  if not is_path_exist:
    print("Please enter a valid existing directory.")
    return get_images_directory()

  return os_home_directory


def get_target_directory():
  user_directory = input("Enter full path to the target directory or press ENTER for the same as source directory: ")

  is_path_exist = Path(user_directory).exists()

  if user_directory and is_path_exist:
    return Path(user_directory) # treated as Path object, which simplifies path manipulation

  if not is_path_exist:
    print("Please enter a valid existing directory.")
    return get_target_directory()
  
  return None


def create_folder(directory, sub_directory):  
  target_folder = directory / sub_directory
  
  if not target_folder.exists():
    target_folder.mkdir(parents=True) # parents=True - will create the final directory and any missing parent directories along the path.
  return target_folder


def extract_image_date(img):
  try:
    image = Image.open(img)
    data = image._getexif() # get the image metadata Exif (Exchangeable Image file format)
    
    if data:
      date = data.get(36867) # DateTimeOriginal

      if not date:
        date = data.get(306)  # DateTime
      
      if date:
        return date.split(' ')[0].replace(':', '-')   

    return None
  
  except Exception as error:
    print(f"\nNo metadata found in '{img}'\nError message: {error}")
    return None


def organize_files(source_dir, target_dir):
  total_files = 0

  # generate the file names in a directory tree by walking the tree bottom-up
  for (root, _ , files) in os.walk(source_dir):
    total_files = len(files)
    
    for i, file in enumerate(files, 1):
      img_file_path = Path(root) / file
      target_sub_folder = extract_image_date(img_file_path)

      if img_file_path and target_sub_folder:
        target_folder = create_folder(target_dir, target_sub_folder)
        
        shutil.move(img_file_path, target_folder / file)

        print(f"\nProcessing image {i} of {total_files}, Moved: '{file}' to '{target_folder}'\n")
      else:
        print(f"Skipped image {i} of {total_files}, No metadata found for '{file}'")

  if total_files == 0:
    print("\nNo files found\n")
    

def main():
  source_directory = get_images_directory()
  target_directory = get_target_directory() or source_directory
 
  print(f"\nSource directory: {source_directory}")
  print(f"Target directory: {target_directory}")
  
  while True:
    user_confirmation = input("Do you want to proceed? (y/n): ")

    if user_confirmation not in ['y', 'n']:
      continue
    else:
      break
    
  if user_confirmation == 'y':
    organize_files(source_directory, target_directory)
  else:
    print("Operation canceled.")


if __name__ == "__main__" : main()