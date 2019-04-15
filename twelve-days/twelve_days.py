def recite(start_verse, end_verse):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    presents = ['a Partridge',
                'two Turtle Doves',
                'three French Hens',
                'four Calling Birds',
                'five Gold Rings',
                'six Geese-a-Laying',
                'seven Swans-a-Swimming',
                'eight Maids-a-Milking',
                'nine Ladies Dancing',
                'ten Lords-a-Leaping',
                'eleven Pipers Piping',
                'twelve Drummers Drumming']

    result = []
    for i in range(12):
        string = ""
        presents_string = ""
        if i > 0:
            counter = i
            while counter > 0:
                presents_string += presents[counter] + ", "
                counter-=1
            presents_string += "and " + presents[0]
        else:
            presents_string = presents[0]
        string = "On the " + days[i] + " day of Christmas my true love gave to me: " + presents_string + " in a Pear Tree."
        result.append(string)

    print(result[0:11])

    return result[start_verse-1:end_verse]
