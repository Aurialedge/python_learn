# function defination
def avg():
    a=int(input("Enter the number 1"))
    b=int(input("Enter the number 2"))
    c=int(input("Enter the number 3"))
    average=float((a+b+c)/3)
    print(average)
# We can all the function any number of time by  using the function call

avg() # function call
# avg()
# avg()

# using the arguments

def Greet(name):
    print(f"Good day {name}")
Greet("Shivraj")
Greet("India")

z=Greet("Shiv")
print(z)
# Does give value of anything as function hasn't returned anything to store in for the z

# Below function will return value
def Greet(name):
    return f"Good day {name}"
m=Greet("Shivraj")
print(m)