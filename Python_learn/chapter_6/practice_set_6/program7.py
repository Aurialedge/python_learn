post=input("Enter the post discription")
n=post.find("Shivraj")
if(n>=0):
    print("The post talks about the Shivraj")
else:
    print ("The post doesn't talk about the Shivraj")

# if you want to avoid the case sensitivity use

if("Shivraj".lower() in post.lower()):
    print("Shivraj is present in the POST")
else:
    print("Shivraj is not present in the POST")