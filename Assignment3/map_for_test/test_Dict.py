import os

path = "/Users/XPS/Desktop/1DV501/assignment_3/me_why.txt"
path_2 = "/Users/XPS/Desktop/1DV501/assignment_3/why_oh_why.txt"

def count_occurences(lst):

    dct_len = []

    for n in lst:
        dct_len.append((len(n), n))
        dct_len.sort()
    return len(dct_len)

print(count_occurences(path_2))

