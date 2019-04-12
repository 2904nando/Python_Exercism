# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

def get_list(word):
    list_temp = []
    for i in word:
        list_temp.append(i)
    return list_temp

def get_str(list):
    result = ""
    for i in list:
        result += i
    return result

def substituir_char(char, index, word):
    word_list = get_list(word)
    word_list[index] = char
    return get_str(word_list)

class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word.lower()
        self.masked_word = "_"*len(self.word)

    def guess(self, char):
        if self.remaining_guesses < 0 or self.get_status() == STATUS_WIN:
            raise ValueError('You lost the game!')
        counter = 0
        acerto = False
        if char in get_list(self.masked_word):
            self.remaining_guesses -= 1
        else:
            for i in self.word:
                if char == i:
                    acerto = True
                    self.masked_word = substituir_char(i, counter, self.masked_word)
                counter += 1
            if acerto == False:
                self.remaining_guesses -= 1

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        if "_" not in get_list(self.masked_word):
            return STATUS_WIN
        elif "_" in get_list(self.masked_word) and self.remaining_guesses >= 0:
            return STATUS_ONGOING
        else:
            return STATUS_LOSE
