def list_from_str(str):
    list_temp = []
    for i in str:
        list_temp.append(i)
    return list_temp

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")
    else:
        hamming_distance = 0
        strand_a_list = list_from_str(strand_a)
        strand_b_list = list_from_str(strand_b)
        for i,val in enumerate(strand_a_list):
            if val != strand_b_list[i]:
                hamming_distance += 1

    return hamming_distance
