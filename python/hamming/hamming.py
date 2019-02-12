def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Sequences not of equal length.")

    return sum(1 for i, nucleotide in enumerate(strand_a) if nucleotide != strand_b[i])