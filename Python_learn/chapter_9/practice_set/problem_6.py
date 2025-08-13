# Path to log file
file_path = r"pythonLearn\Python_learn\chapter_9\practice_set\log.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    content = file.read()

# Case-insensitive search
if "python" in content.lower():
    print("Log file contains the word 'python'.")
else:
    print("Log file does not contain the word 'python'.")
