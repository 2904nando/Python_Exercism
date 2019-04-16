def hey(phrase):

    phrase = phrase.replace("\n", "")
    phrase = phrase.replace("\t", "")
    phrase = phrase.replace(" ", "")

    question_simple = "Sure."
    question_yell ="Calm down, I know what I'm doing!"
    yell = "Whoa, chill out!"
    nothing = "Fine. Be that way!"
    anything_else = "Whatever."


    question = False

    if len(phrase) == 0:
        return nothing

    letters_str = "abcdefghijklmnopqrstuvwxyz1234567890"
    letters_str += letters_str.upper()

    letters = set()

    for letter in letters_str:
        letters.add(letter)

    if phrase[-1] == "?":
        question = True

    isnothing = True
    for i in phrase:
        if i in letters:
            isnothing = False

    if isnothing == True and question == False:
        return nothing

    upper = phrase.isupper()

    if question == True and upper == True:
        return question_yell
    elif question == True and upper == False:
        return question_simple
    elif question == False and upper == True:
        return yell
    elif question == False and upper == False:
        return anything_else
