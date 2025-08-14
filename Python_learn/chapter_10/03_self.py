class Employee:
    language="Python"
    salary=1800000
    def getInfo(self):
        # you can use any name instread of self its just common to use self
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello do greet things")
shiv=Employee()
shiv.language="java"
print(shiv.language)

shiv.getInfo()
# above is converted to the same thing as below
Employee.getInfo(shiv)

# no need to send the self object to the greet() as it is static method
# static method don't need the object method to run
shiv.greet()