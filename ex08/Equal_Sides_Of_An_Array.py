def find_even_index(arr):
    if (arr[0] == sum(arr)):
        return 0
    for i in range(len(arr)):
        if sum(arr[0:i+1]) == sum(arr[i+2:]):
            return i + 1
    if (sum(arr) == 0):
        return 0
    return -1
