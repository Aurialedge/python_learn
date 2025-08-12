#  spam filteration
email=input("Enter the email")
check_list=["Make a lot of money", "buy now", "subscribe this", "click this"]

if (check_list[0] in email or check_list[1] in email or check_list[2] in email or check_list[3] in email ):
    print("Spam")
else:
    print("Not Spam")
