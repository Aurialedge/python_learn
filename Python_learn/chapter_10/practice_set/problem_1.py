class MicrosoftInfo:
    
    def __init__(self, name, salary, position):
        self.name=name 
        self.salary=salary
        self.position=position

    def printInfo(self):
        print(f" Employee Name = {self.name} \n Employee Position = {self.position} \n Salary = {self.salary}")

n=int(input("Enter the number of the Employees"))
for i in range(n):
      name=input("Enter your name")
      salary=int(input("Enter the salary"))
      role=input("Enter your role")
      Shiv=MicrosoftInfo(name, salary,role)
      Shiv.printInfo()