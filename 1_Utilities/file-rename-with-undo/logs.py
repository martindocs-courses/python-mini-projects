import json
from pathlib import Path

# Absolute path. Directory where the logs resides.
LOG_FILE = f"{Path(__file__).resolve().parent}/history_logs.json"

def load_logs():  
  try:
    with open(LOG_FILE, 'r') as log_file:     
      return json.load(log_file)
  except JSONDecodeError: 
    return {}

def save_logs(logs):
  with open(LOG_FILE, 'w') as log_file:
    json.dump(logs, log_file, indent=4)

if __name__ == '__main__': 
  # No invocation here, purely for imports
  pass