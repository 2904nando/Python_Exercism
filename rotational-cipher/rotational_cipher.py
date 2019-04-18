def rotate(text, key):
    letters_str = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    for letter in letters_str:
        letters.append(letter)

    symbols_str = " '1234567890,.!@#$%ˆ&*()"
    symbols = []
    for symbol in symbols_str:
        symbols.append(symbol)

    result = ""

    for letter in text:
        is_upper = letter.isupper()
        letter = letter.lower()
        if letter in symbols:
            result += letter
        elif letter in letters:
            index = letters.index(letter)
            index += key
            if index > 25:
                index = (index % 25) - 1
            
            if is_upper == True:
                result += letters[index].upper()
            else:
                result += letters[index]
            index+=1
    return result
