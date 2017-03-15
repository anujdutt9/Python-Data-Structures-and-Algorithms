# Arrays

arr = [1,2,3,4,5]

# Random Indexing -> O(1) complexity if we know index of
# item to get fromm array
print(arr[1])

# Insert item at given index
# Complexity O(N) to add item at given index
arr[1] = 200
# print(arr[1])

# print all items in array
for num in arr:
    print(num)

# print all items in array using index
for i in range(len(arr)):
    print(arr[i])

# Print out items from starting to ending index
print(arr[0:2])

# Print out whole array
print(arr[:])

# Print out all items of array except last one
print(arr[:-1])

# Linear Search; O(N) time complexity
# If we don't know index, we need to go through whole array sequentially
maxim = arr[0]
for num in arr:
    if num > maxim:
        maxim = num
print(maxim)