# recursive program to calculate the sum of the first n natural numbers

k=int(input("Enter the natural number"))
container=0
def sum(n):
    if(n>0):
        return sum(n-1)+n
    elif(n==0):
        return 0
print(sum(k))