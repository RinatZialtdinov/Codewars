def first_non_repeating_letter(string):
    if len(string) == 0:
        return ""
    copy_s = list()
    for i in string.lower():
        if i not in copy_s:
            copy_s.append(i)
        else:
            copy_s.remove(i)
    if len(copy_s) == 0:
        return ""
    if copy_s[0] in string:
        return copy_s[0]
    else:
        return copy_s[0].upper()
