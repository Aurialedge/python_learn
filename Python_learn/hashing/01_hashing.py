# hashing prototype
def hash_string(s):
    hash_value = 0
    for char in s:
        hash_value += ord(char)
    return hash_value
# Example usage
print(hash_string("hello"))  # Output: 532

# background information
# Hashing is a technique used to uniquely identify data of arbitrary size.
# In this example, we create a simple hash function that sums the ASCII values of characters in a string.