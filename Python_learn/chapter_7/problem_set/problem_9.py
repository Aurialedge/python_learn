# Pattern
n=int(input("Enter the number of rows"))
x=" "
y="*"
print(y*n)
for i in range(n-1):
    print(y+x*(n-2)+y)
print(y*n)