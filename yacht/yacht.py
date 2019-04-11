# Score categories
# Change the values as you see fit
YACHT = 'yatch'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full'
FOUR_OF_A_KIND = 'four_oak'
LITTLE_STRAIGHT = 'little'
BIG_STRAIGHT = 'big'
CHOICE = 'choice'

def calc_simple(dice, number):
    counter = dice.count(number)
    result = number * counter
    return result

def calc_full(dice):
    result = 0
    set_temp = set()
    result_temp = 0
    for i in dice:
        set_temp.add(i)
        result_temp += i
    if len(set_temp) == 2:
        if dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3:
            result = result_temp
        else:
            result = 0
    else :
        result = 0
    return result

def calc_four_oak(dice):
    result = 0
    set_temp = set()
    number = 0
    for i in dice:
        set_temp.add(i)
    for i in set_temp:
        if dice.count(i) >= 4:
            number = i
            break
    if number != 0:
        result = number * 4
    return result

def sort_list(lista):
    lista.sort()
    return lista

def calc_little_big(dice, tipo):
    result = 0
    little = [1,2,3,4,5]
    big = [2,3,4,5,6]
    dice_sorted = sort_list(dice)
    if tipo == 'little':
        if dice_sorted == little:
            result = 30
    else:
        if dice_sorted == big:
            result = 30
    return result

def calc_choice(dice):
    result = 0
    for i in dice:
        result += i
    return result

def calc_yatch(dice):
    init = dice[0]
    if dice.count(init) == 5:
        return 50
    else:
        return 0

def score(dice, category):
    res = 0
    if category == 'ones':
        res = calc_simple(dice, 1)
    elif category == 'twos':
        res = calc_simple(dice, 2)
    elif category == 'threes':
        res = calc_simple(dice, 3)
    elif category == 'fours':
        res = calc_simple(dice, 4)
    elif category == 'fives':
        res = calc_simple(dice, 5)
    elif category == 'sixes':
        res = calc_simple(dice, 6)
    elif category == 'full':
        res = calc_full(dice)
    elif category == 'four_oak':
        res = calc_four_oak(dice)
    elif category == 'little':
        res = calc_little_big(dice, 'little')
    elif category == 'big':
        res = calc_little_big(dice, 'big')
    elif category == 'choice':
        res = calc_choice(dice)
    elif category == 'yatch':
        res = calc_yatch(dice)
    return res
