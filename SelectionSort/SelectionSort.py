# Selection Sort

# Stps:
# 1. Find smallest element in input array
# 2. Swap with left most element in array
# 3. Move to next index
# Sorting in  Ascending Order
def selectionSort(array):
    for i in range(len(array)):
        index = i
        for j in range(i+1, len(array)):
            # Check if element at arr[i+1] < arr[i]
            # If true, swap them
            if array[j] < array[index]:
                index = j
        if index != i:
            swap(array, index, i)
    return array

# Swap element in array
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


# ---------------- Testing --------------------
if __name__ == '__main__':
    a = [1,2,6,4,9,7,8]
    print(selectionSort(a))