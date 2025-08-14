import math
class Calculator:

    def __init__(self,x):
        self.x=x
    def Square(self,x):
        return x*x
    def cube(self,x):
        return x*x*x
    def square_root(self,x):
      return math.sqrt(self.x)


n=int(input("Enter the number"))
    
print(f"Enter your choice \n 1. Square \n 2. Cube \n 3. Square Root \n")

option=int(input(""))
number=Calculator(n)
def switch_case_example(option):
    switch_dict = {
        1: Calculator.Square(number,n),
        2: Calculator.cube(number,n),
        3: Calculator.square_root(number,n)
    }
    return switch_dict.get(option, "Invalid option")

print("Solution:", switch_case_example(option))  # Output: Option 2 selected
