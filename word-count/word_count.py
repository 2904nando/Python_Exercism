def word_count(phrase):

    phrase = phrase.lower()

    accepted_chars = "abcdefghijklmnopqrstuvwxyz'1234567890"
    chars_set=set()
    for i in accepted_chars:
        chars_set.add(i)

    letter_list = []

    for i in phrase:
        letter_list.append(i)


    words = []
    index = 0
    while index < len(letter_list):
        word_temp = ""
        if letter_list[index] in chars_set:
            new_val = letter_list[index]
            while new_val in chars_set:
                word_temp += new_val
                index += 1
                if index < len(letter_list):
                    new_val = letter_list[index]
                else:
                    break
        index+=1
        words.append(word_temp)

    words_new = []
    for word in words:
        if word != '':
            if word[0] == "'":
                word = word[1:-1]
            words_new.append(word)

    words_set = set()

    for word in words_new:
        words_set.add(word)

    result = {}

    for word in words_set:
        result[word] = words_new.count(word)

    print(result)

    return result
