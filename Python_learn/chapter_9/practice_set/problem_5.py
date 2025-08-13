# List of words to censor
censored_words = ["Donkey", "badword", "stupid", "ugly"]

file_path = r"pythonLearn\Python_learn\chapter_9\practice_set\problem4.txt"

# Step 1: Read file content
with open(file_path, "r") as file:
    content = file.read()

# Step 2: Replace each word in the list
for word in censored_words:
    content = content.replace(word, "######")

# Step 3: Write back updated content
with open(file_path, "w") as file:
    file.write(content)

print("All censored words replaced successfully!")
