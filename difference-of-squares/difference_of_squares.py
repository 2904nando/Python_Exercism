def square_of_sum(count):
    result = 0
    for i in range(count):
        result += i+1
    return result**2


def sum_of_squares(count):
    result = 0
    for i in range(count):
        result += (i+1)**2
    return result


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
