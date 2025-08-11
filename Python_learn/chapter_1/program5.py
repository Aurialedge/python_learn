# Label the program written in problem 4 with comments.  
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

# Example usage
if __name__ == "__main__":
    list_directory_contents()          # current directory
    # Or specify a path:
    # list_directory_contents("/path/to/your/directory")
