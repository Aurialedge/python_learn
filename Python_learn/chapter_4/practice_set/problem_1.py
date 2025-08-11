#  Store the value of 7 fruits inputed by the user in a list

fruit = []
for x in range(7):
    fruit.insert(x,input(f"Enter the name of {x+1} fruit: "))

print("The list of fruits is:", fruit)