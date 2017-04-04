# Insertion Sort

# Function for Insertion Sort
def insertionSort(array):
    for i in range(len(array)):
        j = i
        while (j>0 and array[j-1] > array[j]):
            swap(array, j, j-1)
            # print('\nArray after swapping: ',array)
            j = j-1
    return array

# Swap two numbers in array
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


if __name__ == '__main__':

    a = [1,5,3,8,10,100,4]
    print(insertionSort(a))