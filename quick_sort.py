def quicksort(array, left, right):

    if left < right:
        pivot = find_partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)

def find_partition(array, left, right):

    pivot = array[right]

    i = left - 1
    j = left
    while j < right:
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    
    array[i + 1], array[right] = array[right], array[i + 1]

    return i + 1

arr = [2,3,8,9,5,6,5]
quicksort(arr, 0, 6)
print(arr)