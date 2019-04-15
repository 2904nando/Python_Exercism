def score(word):

    result = 0

    points_1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
    points_2 = ['d', 'g']
    points_3 = ['b', 'c', 'm', 'p']
    points_4 = ['f', 'h', 'v', 'w', 'y']
    points_5 = ['k']
    points_8 = ['j', 'x']
    points_10 = ['q', 'z']

    word = word.lower()

    for letter in word:
        if letter in points_1:
            result += 1
        elif letter in points_2:
            result += 2
        elif letter in points_3:
            result += 3
        elif letter in points_4:
            result += 4
        elif letter in points_5:
            result += 5
        elif letter in points_8:
            result += 8
        elif letter in points_10:
            result += 10

    return result
