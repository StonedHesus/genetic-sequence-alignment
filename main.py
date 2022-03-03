def score(first_sequence, second_sequence):
    """
    Compute the score of a sequence based on how different they are from each other.
    The two parameters of the functions are both lists containing values from within the alphabet {A, C, G, T, -},
    where  A, C, G, T are the representation of the corresponding nucleotides whose name commences with that specific
    letter and - is a special character in the language which depicts that an empty case exists at that position,
    a feat which is seldom achieved after a deletion or insertion.

    The result is the score of the two sequences, an integer numeric value, which is computed using the following set
    of rules:

        i)   If the two cases match then the juxtaposition of the sequences gains two points;
        ii)  If the two generate a mismatch then it loses one point;
        iii) If we have a gap, which is the place where we performed an insertion or deletion, than the result loses
             two points.
    """

    result = 0

    for index in range(len(first_sequence)):
        if first_sequence[index] == "-" or second_sequence == "-":
            result -= 2
        elif first_sequence[index] == second_sequence[index]:
            result += 2
        else:
            result += 1

    return result
