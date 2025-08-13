# Step 1: Read the file
with open(r"pythonLearn\Python_learn\chapter_9\practice_set\problem4.txt", "r") as file:
    content = file.read()

# Step 2: Replace the word
content = content.replace("Donkey", "######")

# Step 3: Write the updated content back
with open(r"pythonLearn\Python_learn\chapter_9\practice_set\problem4.txt", "w") as file:
    file.write(content)

print("Word replaced successfully!")
