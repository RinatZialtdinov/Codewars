def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    elif len(array1) == 0 and len(array2) == 0:
        return True
    array1 = [i ** 2 for i in array1]
    return sorted(array1) == sorted(array2)
