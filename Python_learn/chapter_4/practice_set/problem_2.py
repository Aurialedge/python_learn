#  Accept the marks of the 6 students in a class and than display it in the sorted order
marks = []
for i in range(6):
    marks.append(int(input(f"Enter the marks of student {i+1}: ")))
marks.sort()  # sorts the list in ascending order
print("The sorted marks of the students are:", marks)