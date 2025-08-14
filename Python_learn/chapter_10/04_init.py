class Employee:
    language="Python"
    salary=1800000

    def __init__(self, name, salary, language): # dunder method which is automatically called when object is made of this class
        print("HEllo")
        self.name=name
        self.salary=salary
        self.language=language
    def getInfo(self):
        # you can use any name instread of self its just common to use self
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello do greet things")
# shiv=Employee()
# shiv.language="java"
# print(shiv.language)

shiv=Employee("Shivraj", 5000000, "Java")


# shiv.getInfo()
# above is converted to the same thing as below
# Employee.getInfo(shiv)

# no need to send the self object to the greet() as it is static method
# static method don't need the object method to run
# shiv.greet()