# Key: Value
dict = {'Joe': 22, 'Adam': 26, 'Emily': 56}

# O(1) time complexity
print(dict['Joe'])

dict['Joe'] = 24
print(dict['Joe'])

# Print all values in the Dictionary
print(dict.items())

# Print all the Key values
print(dict.keys())

# Print all values in Dictionary
# Values are not printed in same order
print(dict.values())

# Clear all entries in the Dictionary
dict.clear()

print(dict.values())

# Delete the Dictionary
del dict

# ------------------------ EOC -----------------------