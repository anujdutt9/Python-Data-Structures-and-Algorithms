# Bubble Sort

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
    return arr

# Swap Elements of Array
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


# ------------- Testing ----------------
if __name__ == "__main__":
    array = [1,5,3,2,4,8,7]
    print(bubbleSort(array))
