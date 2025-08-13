with open(r"pythonLearn\Python_learn\chapter_9\practice_set\poem.txt", "r") as x:
    lines = x.readlines()

count = 0

for line in lines:
    if "twinkle" in line.lower():  # case-insensitive match
        count += 1

if count == 0:
    print("This poem doesn't contain the word 'twinkle'")
else:
    print(f"This poem contains the word 'twinkle' {count} time(s)")

    #  another way of doing 
    
