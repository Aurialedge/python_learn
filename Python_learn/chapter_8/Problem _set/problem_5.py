x="*"
n1=int(input("Enter the value of rows"))

def pattern(n):
    if(n>0):
        print(x*n)
        return pattern(n-1)
    else:
        return 0
pattern(n1)
    