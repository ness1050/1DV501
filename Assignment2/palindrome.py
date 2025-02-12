# Inside file palindrome.py, 
# create a function is_palindrome(s) that returns True only 
# if the string s is a palindrome.
# A string is a palindrome if it contains the same sequence of letters when read backwards. We make no difference between upper and lower case letters. Examples of palindromes are:
 

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
