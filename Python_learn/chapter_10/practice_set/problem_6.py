class Demo:
    def __init__(harry, name):  # here 'harry' is like 'self'
        harry.name = name

    def greet(harry):
        print(f"Hello, my name is {harry.name}")

# Create object
obj = Demo("Krishna")
obj.greet()
