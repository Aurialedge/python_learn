# Check if the number is prime or not

x=int(input("Enter the number"))

for i in range(2,x):
    if(x%i==0):
        print("The number is not the prime")
        break
else:
    print("Number is prime")