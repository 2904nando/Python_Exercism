def raindrops(number):
    factors=[]
    for i in range(1, number+1):
        if number%i == 0:
            factors.append(i)
    print(factors)
    result = ""
    if 3 in factors:
        result+="Pling"
    if 5 in factors:
        result+="Plang"
    if 7 in factors:
        result+="Plong"
    if result == "":
        result = str(number)
    return result
