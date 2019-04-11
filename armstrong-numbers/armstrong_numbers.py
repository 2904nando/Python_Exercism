def is_armstrong(number):
    size = len(str(number))
    result = 0
    for i in str(number):
        result += int(i)**size
    return True if result == number else False
