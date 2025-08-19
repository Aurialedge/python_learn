# operator overloading
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"
    def __add__(self, other):
        if isinstance(other, Employee):
            return Employee(self.fname + " " + other.fname, self.lname + " " + other.lname)
        return NotImplemented
e1=Employee("Shivraj", "Perkar")
e2=Employee("John", "Doe")
print(e1 + e2)