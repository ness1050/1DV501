


from random import randint

# printer ut antal random numbers i listan
def random_list(n):
    list = []
    for i in range(n):
        random_number = randint(1, 100)
        list.append(random_number)
    return list

#hittar average i listan
def average(t):
    sum_number = 0
    for i in t:
        sum_number = sum_number + i
    average_number = sum_number / len(t)
    return round (average_number)

# kollar efter udda tal bara
def only_odds(lst):
    odd_list = []

    for i in lst:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

# ska göra de till en string
def tostring(lst):
    string = " "

    for i in(lst):
        string += f'{str(i)}, '
    return string

# kollar om den a följs av b i rätt ordning
def contains(lst, a , b):
    range_lst = len(lst)
    for i in range(range_lst):
        if lst[i] == a:
            if lst [i + 1] == b :
                return True
    return False

# kollar om det finnns duplicates
def has_duplicates(s):

    list_set = []
    set_list = set(list_set)

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
         if s[i] == s[j]:
                return True
         break
        else:
             return False 
    return list_set