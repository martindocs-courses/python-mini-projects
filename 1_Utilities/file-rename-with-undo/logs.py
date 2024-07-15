import json
from pathlib import Path

# Absolute path. Directory where the logs resides.
LOG_FILE = f"{Path(__file__).resolve().parent}/history_logs.json"

def load_logs():  
  try:
    with open(LOG_FILE, 'r') as log_file:     
      return json.load(log_file)
  except Exception as error: 
    return {}

def save_logs(logs):
  with open(LOG_FILE, 'w') as log_file:
    json.dump(logs, log_file, indent=4)

def list_logs():
  logs = load_logs()
  log_list = []

  if not logs:
    print("\nNo logs found.\n")
  else:
    for timestamp, log in logs.items():
      summary = log['summary']

      log_entry = f"\n{timestamp} - {summary['file_count']} files renamed:\nTarget folder: {summary['directory']} \nWith prefix: '{summary['prefix']}'." 

      for example in summary['example']:
        log_entry += f"\nExample: \nOld: {example['old']} \nNew: {example['new']}\n"
      
      log_list.append(log_entry)

  return log_list      


if __name__ == '__main__': 
  # No invocation here, purely for imports
  pass