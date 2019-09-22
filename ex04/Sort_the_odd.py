def sort_array(source_array):
    new_list1 = []
    new_list2 = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            new_list1.append(i)
            new_list2.append(source_array[i])
    new_list2 = sorted(new_list2)
    k = 0
    for i in new_list1:
        source_array[i] = new_list2[k]
        k += 1
    return source_array
