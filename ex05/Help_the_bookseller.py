def stock_list(listOfArt, listOfCat):
    num = 0
    result = ""
    k = 0
    for i in listOfCat:
        for j in listOfArt:
            if i == j[0]:
               num = num + int(j.split()[1])
        if num == 0:
            k += 1
        result = result + "(" + i + " : " + str(num) + ") - "
        num = 0
    if k == len(listOfCat):
        return("")
    return (result[:-3])
