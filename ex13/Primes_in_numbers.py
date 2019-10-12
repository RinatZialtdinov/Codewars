def primeFactors(n):
    k = 2
    list = []
    while n != 1:
        if n % k == 0:
            n = n // k
            list.append(k)
        else:
            k = k + 1
    number = set(list)
    number = sorted(number)
    result = ""
    i = 0
    while i != len(number):
        if list.count(number[i]) == 1:
            result = result + "(" + str(number[i]) + ")"
        else:
            result = result + "(" + str(number[i]) + "**" + str(list.count(number[i])) + ")"
        i = i + 1
    return result
