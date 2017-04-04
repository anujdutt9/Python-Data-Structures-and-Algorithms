# Merge Sort

def mergeSort(array):
    if len(array) == 1:
        return
    middle = len(array) // 2

    left_half = array[:middle]
    right_half = array[middle:]

    mergeSort(left_half)
    mergeSort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        k += 1
        i += 1


# ----------------- Testing -------------------
if __name__ == '__main__':
    a = [-3,-2,-1,1,2,1,0,-1,-2,-3]
    mergeSort(a)
    print(a)

# ----------------------------- EOC ------------------------