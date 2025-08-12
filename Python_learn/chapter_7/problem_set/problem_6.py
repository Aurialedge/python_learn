# Finding the factorial of the number
n=int(input("Enter the number"))
pro=1
for i in range(1,n+1):
    pro*=i
print(pro)