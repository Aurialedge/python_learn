class Employee:
    a=1
class Programmer( Employee):
    b=2
class Manager( Programmer):
    c=3
sample=Employee()
print(sample.a)
# print(sample.b)
# This will raise an AttributeError

sample2=Programmer()
print(sample2.a, sample2.b)
# but i can't access sample2.c