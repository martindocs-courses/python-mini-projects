import os
from datetime import datetime
from logs import load_logs, save_logs

def rename_files(dir, prefix):
  
  target_files = os.listdir(dir)  
  timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # example 2024-07-01 21-43-50
  rename_log = load_logs() 
  
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
    "old": old_file_path})
  
  rename_log[timestamp] = {
    "summary": {
      "directory": dir,
      "prefix": prefix,
      "file_count": len(target_files),
      "example": show_example 
    },
    "files": file_mappings
  }
 
  save_logs(rename_log)

  print(f"\nRenamed {len(target_files)} files.\n")


def rename_undo(timestamp):
  logs = load_logs()

  if timestamp in logs:
    for new_file_path, old_file_path in logs[timestamp]['files'].items():

      if os.path.exists(new_file_path):
        os.rename(new_file_path, old_file_path)
    
    del logs[timestamp]

    save_logs(logs)
    print(f"\nRenamed files for {timestamp} have been successfully undone.\n")

  else:
    print(f"\nNo logs found for {timestamp}.\n")

if __name__ == '__main__': 
  # No invocation here, purely for imports
  pass