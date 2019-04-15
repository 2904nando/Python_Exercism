def abbreviate(words):

    words = words.upper()

    words = words.replace("\n", " ")
    words = words.replace(",", " ")
    words = words.replace("-", " ")
    words = words.replace("_", "")

    words += "."

    chars_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ'"

    chars = set()

    for char in chars_str:
        chars.add(char)

    words_separated = []

    temp_str = ""

    for char in words:
        if char in chars:
            temp_str += char
        else:
            if len(temp_str) > 0:
                words_separated.append(temp_str)
                temp_str = ""

    acronym = ""
    for word in words_separated:
        acronym += word[0]

    return acronym
