# Path to the log file
file_path = r"pythonLearn\Python_learn\chapter_9\practice_set\log.txt"

found = False  # flag to track if 'python' is found

with open(file_path, "r") as file:
    for line_no, line in enumerate(file, start=1):
        if "python" in line.lower():  # case-insensitive check
            print(f"'python' found on line {line_no}: {line.strip()}")
            found = True

if not found:
    print("Log file does not contain the word 'python'.")
