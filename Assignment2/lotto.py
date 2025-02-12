# The Swedish Lotto
# works by randomly selecting seven of 35 numbers (in sequence). 
# Write a program called lotto.py which creates a valid lotto sequence, that is seven numbers in the range from 1 to 35 in ascending order without duplicates.
# See below for an example execution:

from random import randint
# lotto = list 
list = []

for i in range(7):
    number = randint(1, 35)
    while number in list:
        number = randint(1, 35)
    list.append(number)
    
list.sort()
print("the lotto number this week:", list)






