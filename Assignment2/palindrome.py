
def only_small(k):

    for i in range(32, 97):
        k = k.replace(chr(i), '')
    for i in range(123, 127):
        k = k.replace(chr(i), '')

    return k


def palindrome(s):
    s = s.lower()
    l = len(s)
    reverse = only_small (s[::-1])
    if l < 2:
        return True 
    elif s[0] == s[l - 1]:
        return True
    else:
        return False
    
   

print(palindrome("aba"))
