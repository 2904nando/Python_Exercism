def is_isogram(string):
    verify_list = []
    isogram = True
    for i in string.lower():
        if i == " " or i == "-":
            continue
        else:
            if i in verify_list:
                isogram = False
                break
            verify_list.append(i)
    return isogram
