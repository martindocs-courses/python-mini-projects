"""
Description: Create a script that sends automated emails at scheduled times. 

Steps:
1 - setup the stmp server
2 - email content builder
3 - user input handling
4 - method for scheduling emails
5 - handling any errors
6 - any additional helper methods

Concepts: Networking, file I/O, Scheduling, Security

"""

from stmp_server import server

def main():
  ser = server()
  print(ser)


if __name__ == "__main__": main()