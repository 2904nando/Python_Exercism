def onlyNumbersAndX(str):
    str = str.upper()
    chars = set()
    chars_str = '1234567890X'
    for char in chars_str:
        chars.add(char)

    result = ""
    for i in str:
        if i in chars:
            result += i

    return result

def verify(isbn):
    isbn = onlyNumbersAndX(isbn)

    if len(isbn) != 10:
        return False

    local_x = isbn.find("X")

    if local_x != -1 and local_x != (len(isbn)-1):
        return False

    else:
        result = 0
        counter = 10
        for num in isbn:
            if num != "X":
                num = int(num)
            else:
                num = 10
            result += num * counter
            counter -= 1

        if result % 11 == 0:
            return True
        else:
            return False
