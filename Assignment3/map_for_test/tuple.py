
'''tpl = tuple(range(1, 5))
print(tpl)
print(len(tpl))
print(max(tpl))
print(min(tpl))
print(sum(tpl)) '''




def count_different(lst):

   myset = set()
   for i in lst:
       print(i, end=" ")
       myset.add(i)
   return len(myset)


myset = [1, 1,7,8,
 2, 3 ,5 ,5]

print(count_different(myset))

def count_occurences(lst):

    dct = {} 
    k = d.keys()
    v = d.values()

    for item in lst:
        if item in k:
            k +=1
        if item in v:
            v += 1
        





