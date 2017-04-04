# Quick Sort Algorithm

# Quick Sort
def quickSort(array, low, high):
    if low >= high:
        return
    pivot = partition(array, low, high)
    quickSort(array, low, pivot-1)
    quickSort(array, pivot+1, high)
    return

# Functioon for Partitioning the Array
def partition(array, low, high):
    pivotIndex = (low+high)//2
    swap(array, pivotIndex, high)

    i = low
    # Sorting in Ascending Order
    for j in range(low, high):
        if array[j] <= array[high]:
            swap(array, i,j)
            i += 1
    swap(array, i, high)
    return i

# Swap two values
def swap(arr, x,y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


# ------------- Testing -----------------
if __name__ == '__main__':
    a = [1,5,3,7,9,4,100]
    quickSort(a, 0, len(a)-1)
    print(a)