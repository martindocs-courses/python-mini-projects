import os
from datetime import datetime

def rename_files(dir, prefix):
  
  target_files = os.listdir(dir)  
  timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # example 2024-07-01 21-43-50
  rename_log = {} # load logs method
  
  show_example = []
  file_mappings = {}

  for file in target_files:
    
    # skip hidden files
    if not file.startswith("."):
      
      old_file_path = os.path.join(dir, file)
      new_file_name = prefix + file
      new_file_path = os.path.join(dir, new_file_name)

      # rename the file with the new prefix
      os.rename(old_file_path, new_file_path)

      file_mappings[new_file_path] = old_file_path

  show_example.append({
    "new": new_file_path, 
    "old": old_file_path}
  )
  
  rename_log[timestamp] = {
    "summary": {
      "directory": dir,
      "prefix": prefix,
      "file_count": len(target_files),
      "example": show_example 
    },
    "files": file_mappings
  }

  print(rename_log)

  # method for save_logs

  print(f"Renamed {len(target_files)} files.")


def rename_undo(timestamp):
  pass


if __name__ == '__main__': 
  # No invocation here, purely for imports
  pass