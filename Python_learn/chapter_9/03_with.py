f=open(r"s:\Skills\Python\pythonLearn\Python_learn\chapter_9\file.txt")
print(f.read())
f.close()

# The same can be written with the statement like this
with open(r"s:\Skills\Python\pythonLearn\Python_learn\chapter_9\file.txt") as f:
    print(f.read())
# here we dont have to explicitly closem the file
