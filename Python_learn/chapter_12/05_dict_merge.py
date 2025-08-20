dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

with (
    open("file1.txt") as f1,
    open("file2.txt") as f2,
    open("file3.txt") as f3
):
    data1 = f1.read()
    data2 = f2.read()
    data3 = f3.read()
