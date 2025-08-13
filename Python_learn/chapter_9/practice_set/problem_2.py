x=open(r"pythonLearn\Python_learn\chapter_9\practice_set\highest.txt")
n=x.read()
n=x.readline()
x.close()
updatedscore="80"
x=open(r"pythonLearn\Python_learn\chapter_9\practice_set\highest.txt","w")
x.write(updatedscore)
x.close()