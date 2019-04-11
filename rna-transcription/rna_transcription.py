def to_rna(dna_strand):
    dict_transcript = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    result=""
    for i in dna_strand:
        result += dict_transcript[i]
    return result
