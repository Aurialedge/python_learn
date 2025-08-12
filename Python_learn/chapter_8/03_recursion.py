def factorial( n,pro):

    if (n>0):
        pro*=n
        n-=1
        return factorial(n,pro)
    else:
        return pro

n=int(input("Enter the number"))
answer=factorial(n,1)
print(answer)

# Method 2
def factorial2(n):
   if(n==0 or n==1):
       return 1
   return n*factorial(n-1)