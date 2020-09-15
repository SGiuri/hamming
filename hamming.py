def distance(strand_a, strand_b):

    # Check equal Lenght

    if len(strand_a) != len(strand_b):
        raise ValueError("Equal length not verified")

    # set up a counter of differences
    hamming_difference = 0

    # checking each letter
    for j in range(len(strand_a)):
        # if there is a difference, increasing the hamming difference by 1
        if strand_a[j] != strand_b[j]:
            hamming_difference += 1

    return hamming_difference

