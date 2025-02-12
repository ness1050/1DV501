# Write a program countdigits
# which for any given positive number N
# (read from the keyboard) prints the number of zeros, odd digits, 
# and even digits of the integer.  
    
def counter():
    odd = 0
    user = int(input("Enter a number: "))
    even = 0
    zero = 0
    for digit in str(user):
        if digit == '0':
            zero += 1
        elif int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Odd digits: {odd}, Even digits: {even}, Zeros: {zero}")

    return odd, even, zero


    
counter()