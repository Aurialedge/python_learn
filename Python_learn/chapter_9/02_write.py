st="I am done with this"

f = open()

lines=f.readlines()
# readline() is for reading 1 line and the readlines is usd for the reading the complete lines

# print(lines) 
print(lines, type(lines))


#  for appending text use the append mode mode ="a"
# f.write(st) for writing st
f.close()