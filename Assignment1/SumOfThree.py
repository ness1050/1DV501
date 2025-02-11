

# A VG task
# To take a three number of integer and return the sum of those numbers

def sum(number):
    total = 0
    
    while(number > 0):
        digit = number % 10
        total+= digit
        number = number // 10
    return total

def main():
    ui = int(input("Enter a three digit number: "))
    print(f'The sum of the digit is: {sum(ui)}')
    
main()