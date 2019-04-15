def get_total_from_nums(list):
    list_num_chars = []
    counter = 0
    for num_char in list[::-1]:
        num_char = int(num_char)
        if counter%2 != 0:
            num_char *= 2
            if num_char >= 10:
                num_char -= 9
        counter += 1
        list_num_chars.append(num_char)

    result = 0

    for i in list_num_chars:
        result += i

    return result


class Luhn(object):
    def __init__(self, card_num):
        self.nums = card_num.replace(" ", "")

    def is_valid(self):

        invalid_chars_str = "!@#$%ˆ&*()',-_abcdefghijklmnopqrstuvwxyz:"

        invalid_chars = set()

        for char in invalid_chars_str:
            invalid_chars.add(char)

        for char in invalid_chars:
            for char in invalid_chars:
                if char in self.nums:
                    return False

        if len(self.nums) == 1:
            return False

        list_nums = []

        for i in self.nums:
            list_nums.append(i)

        print(list_nums)

        total = get_total_from_nums(list_nums)

        if total % 10 == 0:
            return True
        else:
            return False
