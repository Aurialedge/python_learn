# Q4) Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that. 

import os

def list_directory_contents(path='.'):
    """Prints all entries (files and directories) in the given directory."""
    try:
        entries = os.listdir(path)
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except OSError as e:
        print(f"Error accessing directory '{path}': {e}")


if __name__ == "__main__":
    list_directory_contents()          
  
