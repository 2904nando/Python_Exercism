def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    used_letters = set()
    for i in sentence:
        if i in alphabet:
            used_letters.add(i)
    if len(used_letters) == len(alphabet):
        return True
    else:
        return False
