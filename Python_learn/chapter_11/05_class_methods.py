class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"Employee a: {cls.a}")

# A class method is bound to the class and not to the object of the class
e=Employee()
e.a=45
e.show()