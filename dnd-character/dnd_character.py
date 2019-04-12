from random import randint

def roll_dice():
    return randint(1,6)

def get_value_from_dice():
    list_temp = []
    for i in range(4):
        list_temp.append(roll_dice())
    min_value = 6
    min_index = 0

    sum = 0
    for index, val in enumerate(list_temp):
        if val < min_value:
            min_value = val
            min_index = index
        sum += val
    sum -= min_value
    return sum

def modifier(constitution):
    res_temp =  (constitution-10)/2
    result = 0
    if res_temp%1 != 0 and res_temp < 0:
        result = int(res_temp-1)
    else:
        result = int(res_temp)
    return result

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.modifier = modifier(self.constitution)
        self.hitpoints = 10 + self.modifier

    def ability(self):
        return get_value_from_dice()
