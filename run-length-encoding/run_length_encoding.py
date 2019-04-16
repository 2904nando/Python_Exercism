def decode(string):
    num = ""
    result = ""
    for char in string:
        if char in "0123456789":
            num += char
        else:
            print(num)
            if len(num) > 0:
                result += int(num)*char
            else:
                result += char
            num = ""
            
    return result


def encode(string):
    focus = ""
    counter = 1
    result = ""
    for letter in string:
        if focus == "":
            focus = letter
        else:
            if focus == letter:
                counter += 1
            else:
                if counter == 1:
                    result += focus
                else:
                    result+= str(counter) + focus
                focus = letter
                counter = 1

    if counter == 1:
        result += focus
    else:
        result+= str(counter) + focus

    return result
