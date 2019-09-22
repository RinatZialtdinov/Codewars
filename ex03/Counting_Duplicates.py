def duplicate_count(text):
    text = text.lower()
    my_dict = {}
    count = 0
    for i in text:
        if i in my_dict:
            my_dict[i] +=1
        else:
            my_dict[i] = 1
    for i in my_dict.values():
        if i != 1:
            count +=1
    return count
