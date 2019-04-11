from random import randint

def get_random_letter():
    letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return letters[randint(0,24)].upper()

def generate_name():
    l1 = get_random_letter()
    l2 = get_random_letter()
    n1 = randint(0,9)
    n2 = randint(0,9)
    n3 = randint(0,9)
    name = l1 + l2 + str(n1) + str(n2) + str(n3)
    return name

names_used = set()

def test_name_notused():
    name_temp = generate_name()
    while name_temp in names_used:
        name_temp = generate_name()
    names_used.add(name_temp)
    return name_temp

class Robot(object):
    def __init__(self):
        self.name = test_name()
    def reset(self):
        self.name = test_name()
