# that prints all the numbers from 100 to 200, ten per line,
# that are divisible by 4 or 5, but not both.
# The numbers in a printed line are separated 
# by exactly one space


def divisible():
    a = 5
    b = 4
    newlist = []
    for i in range(100, 201):
        if (i % 4 == 0) ^ (i % 5 == 0):
            newlist.append(i)

    for idx, num in enumerate(newlist):
        if idx % 10 == 0 and idx != 0:
            print()
        print(num, end=' ')
    print()

divisible()
    