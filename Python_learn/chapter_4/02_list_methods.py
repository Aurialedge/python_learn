shivraj=[1,34,"hi",2.5,True]
# list are mutable we can change it
# when we apply the method on the sring the original string is not changed
# but when we apply the method on the list the original list is changed

shivraj.append("hello")  # adds an element to the end of the list
print(shivraj)

l1=[23,45,67,89]
l1.sort()  # sorts the list in ascending order
print(l1)

# sorting the list in descending order
l1.sort(reverse=True)
print(l1)
# reversing the list
l1.reverse()
print(l1)

# usingn the insert method to add an element at a specific index
l1.insert(2, 100)  # inserts 100 at index 2

# using the pop method to remove an element at a specific index and return it
removed_element = l1.pop(2)  # removes the element at index 2
# Its not to return the element at index 2
l1.pop(3)


# remove method removes the first occurrence of a value from the list

l1.remove(67)
print(l1)
