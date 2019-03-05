def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(arr1, arr2):

    i = 0
    j = 0
    ret_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ret_arr.append(arr1[i])
            i += 1
        else:
            ret_arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ret_arr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ret_arr.append(arr2[j])
        j += 1
    
    return ret_arr

arr = [5,3,2,8,1,4]
print(merge_sort(arr))