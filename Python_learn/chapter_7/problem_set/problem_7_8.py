# Printing the pattern

n=int(input("Enter the number of rows"))
x=" "
y="*"
for i in range(n):
    print(x*(n-i-1)+ y * (2 * i + 1))

# for printing in different form
# observe the difference
for i in range(n):
    print(y * (2 * i + 1))