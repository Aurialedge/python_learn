x=open(r"pythonLearn\Python_learn\chapter_9\practice_set\this.txt")
z=x.read()

with open(r"pythonLearn\Python_learn\chapter_9\practice_set\copy.txt","w") as y:
    y.write(z)
