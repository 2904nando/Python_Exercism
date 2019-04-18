def slices(series, length):

    result = []

    if length > len(series) or length <= 0:
        raise ValueError("Length value must not be greater then the serie's length!")
        result.append(-1)
        return result
    elif length == len(series):
        result.append(series)
        return result
    else:
        times = len(series) - length + 1
        for serie in range(times):
            temp_serie = ""
            for char in range(length):
                temp_serie += series[char+serie]
            result.append(temp_serie)
    return result
