file1_path = r"pythonLearn\Python_learn\chapter_9\practice_set\file11.txt"
file2_path = r"pythonLearn\Python_learn\chapter_9\practice_set\file12.txt"

is_identical = True

with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
    for line_no, (line1, line2) in enumerate(zip(f1, f2), start=1):
        if line1 != line2:
            print(f"Difference found on line {line_no}")
            is_identical = False

# Also check if one file has extra lines
if is_identical:
    with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
        if len(f1.readlines()) != len(f2.readlines()):
            print("Files differ in length.")
            is_identical = False

if is_identical:
    print("✅ The files are identical.")
else:
    print("❌ The files are different.")
