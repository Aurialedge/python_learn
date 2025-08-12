print("Enter the marks in 3 subject")
arr=[]
sum=0
for i in range(3):
    arr.append(int(input("")))
    if (arr[i]<0 or arr[i]>100):
        print("enter the valid marks")
    else:
        sum+=arr[i]
sum/=3
if(sum>=40):
    for i in range(3):
         if(arr[i]<33):
             print(f"You have not qualified in subject {i}")
             break
    print("You are passed")
else:
    print("You are failed")
