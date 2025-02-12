#import os 

'''def read_File(file_path):

    list = []
    n_file = open(file_path, "r")

    for entry in n_file:'''

import os
path = "/Users/XPS/Desktop/1DV501/assignment_3/why_oh_why.txt"
def read_file(file_path):

    lst = []
    with open (file_path, "r", encoding="utf-8") as file:
        for line in file:
            n = (line.strip())
            lst.append(n)
    return lst

file_path = read_file(path)
print(file_path)

