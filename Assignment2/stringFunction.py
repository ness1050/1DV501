

import math
from typing import List

def concat(s, n):
    return_n = s * n
    return return_n

# checks x in string
def count(s, x):
     x_times=0
     for letter in s:
         if letter == x:
             x_times +=1
     return x_times

# to reverse a string 
def reverse(s):
    reverse_s = s[::-1]
    return reverse_s

# function of first and last string.
def first_last(s):
    first_letter = s[0]
    last_letter = s[len(s)-1]
    return first_letter, last_letter

# two X

def has_two_X(s):
    x_count = 0

    for i in s:
        if i == "x" or i == "X":
            x_count += 1
        if x_count > 2:
            break
    if x_count == 2:
        return True
    return False


#finding duplicates

def has_duplicates(s):
    
    for i in (s):
        if s.count(i) >= 2 :
            return True
    return False



