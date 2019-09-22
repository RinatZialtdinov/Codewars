def duplicate_encode(word):
    word = word.upper()
    new_str = ""
    a = {}
    for i in word:
        if i in a:
            a[i] +=1
        else:
            a[i] = 1
    for i in word:
        if a[i] != 1:
            new_str += ")"
        else:
            new_str += "("
    return new_str
