import os

# Original file path
old_name = r"pythonLearn\Python_learn\chapter_9\practice_set\file12.txt"

# New file name (same folder)
new_name = r"pythonLearn\Python_learn\chapter_9\practice_set\renamed_by_python.txt"

# Rename the file
os.rename(old_name, new_name)

print("✅ File renamed successfully!")
