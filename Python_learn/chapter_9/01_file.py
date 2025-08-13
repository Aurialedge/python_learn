f = open(r"s:\Skills\Python\pythonLearn\Python_learn\chapter_9\file.txt")

#  syntax of this is f=open(<file_name>,<mode>) default mode is read 
# <mode>=r for default mode
data=f.read()
print(data)
f.close()