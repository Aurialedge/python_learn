marks={
    "Yuva": 85,
    "Shivraj": 90,
    "Harsh": 95,
}

print(marks.items())
print(marks.keys())
print(marks.values())

# updating a value
marks.update({"Yuva": 88})
#  We can also add a new key-value pair with the update method
marks.update({"Kurani": 85})

# usingf the get method
print ("Shivraj's marks are", marks.get("Shivraj"))


# important difference between get and direct access
# print(marks.get("Kurani2")) # This will return None if "Kurani2" does not exist
# print(marks["kurani2"])  # This will raise a KeyError if "kurani2" does not exist

# some more methods

# marks.clear()  # This will clear the dictionary

mark_new=marks.copy()  # This will create a shallow copy of the dictionary

# fromkeys method
new_dict = dict.fromkeys(marks,0)  # This will create a new dictionary with keys from 'keys' and all values set to 0
print(new_dict)

# pop and popitem methods
marks.pop("Yuva")  # This will remove the key "Yuva" and return its value
print(marks)
arr=marks.popitem()  # This will remove the last inserted key-value pair and return it
print("Last inserted item:", arr)