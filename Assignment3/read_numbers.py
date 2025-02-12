import os

def count_different(lst):
    numbers = set()

    # A set is a quick way of finding the unique numbers
    for num in lst:
        numbers.add(num)
    return numbers


def count_occurences(lst):
    numbers = {}

    for num in lst:
        # If not already in dictionary, initialize key-value
        if num not in numbers:
            numbers[num] = 0
        # If in dictionary, increment value
        else:
            numbers[num] += 1
    # Simple sort with lambda function
    numbers = numbers.items()
    value_sorted = sorted(numbers, key=lambda tpl: tpl[1], reverse=True)
    # Return sorted list
    return value_sorted


def read_file(path):
    lst = []
    # Read the file and split its values by a given delimiter
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            list = line.split()
            for item in list:
                lst.append(item)
    return lst


lst = read_file("/Users\XPS\Desktop/1DV501/assignment_3/10000_integers/file_10000integers_A.txt")
print(f"There are {len(count_different(lst))} unique integers")
print("The 5 most common of which are: \n")
for kvt in count_occurences(lst)[:5]:
    print(f"{kvt[0]} which occurred {kvt[1]} times")
print("\n")




