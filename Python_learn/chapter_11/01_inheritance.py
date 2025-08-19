class Employee:
    company="ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class new_extended(Employee):
    company="Microsoft"
    def info(self):
        print(f"I am dangerous so I got the admission in the {self.company}")

print(Employee.company, new_extended.company)