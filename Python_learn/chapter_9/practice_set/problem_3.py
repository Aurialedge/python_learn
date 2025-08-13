# Multiplication of 2 to 20 tables in folder

for x in range(20):
    z = rf"pythonLearn\Python_learn\chapter_9\practice_set\table\table{x+2}.txt"
    with open(z, "a") as y:
        for a in range(10):
                y.write(f"{x} X {a} = {x*a} \n")


