# Printing the letter template with the name and date

name=input("Enter your name: ")
date=input("Enter the date: ")

# Using f-string for formatting the letter
print(f"Dear {name},\n\nI hope this letter finds you well. Today is {date}.\n\nBest regards,\nYour Friend")  # Output: Letter template with name and date

# Another way of representing the string

z="""
Dear {name},
I hope this letter finds you well. Today is {date}.
Best regards,"""

print(z.format(name=name, date=date))  # Output: Letter template with name and date using format method