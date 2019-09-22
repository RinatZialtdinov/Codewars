import string

def is_pangram(s):
    a = string.ascii_lowercase
    s = s.lower()
    check = 0
    for i in a:
        for j in s:
            if i == j:
                check = 1
                break
        if check == 1:
            check = 0
        else:
            return False
    return True
