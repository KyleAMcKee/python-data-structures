def find_rotation_point(arr, start, end):

    if start > end:
        return

    mid = (start + end) // 2
    if arr[mid] > arr[mid + 1]:
        return mid
    if arr[mid] > arr[0]:
        return find_rotation_point(arr, mid + 1, end)
    elif arr[mid] < arr[0]:
        return find_rotation_point(arr, start, mid - 1)

def binary_search_iter(arr, num):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] > num:
            end = mid - 1
        elif arr[mid] < num:
            start = mid + 1
        else:
            return mid
    
    return -1

def binary_search_recurse(arr, num, start, end):

    if start > end:
        return

    mid = (start + end) // 2
    if arr[mid] > num:
        return binary_search_recurse(arr, num, start, mid - 1)
    elif arr[mid] < num:
        return binary_search_recurse(arr, num, mid + 1, end)
    return mid

def rotated_binary_search(arr, num):
    if arr[0] <= arr[-1]:
        return binary_search_recurse(arr, num, 0, len(arr) - 1)
    else:
        rotation_point = find_rotation_point(arr, 0, len(arr) - 1)
        if num < arr[0]:
            return binary_search_recurse(arr, num, rotation_point + 1, len(arr) - 1)
        else:
            return binary_search_recurse(arr, num, 0, rotation_point)


arr = [1,2,3,4,5,6,7,8]
# for i in range(1, 8):
#     print(binary_search_iter(arr, i))

# for i in range(1, 8):
#     print(binary_search_recurse(arr, i, 0, len(arr) - 1))

arr1 = [5, 9, 12, 17, 2, 4]
print(rotated_binary_search(arr1, 17))