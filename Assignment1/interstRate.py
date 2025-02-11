

# Task to calculate the 5-years interst rates of a given saving

# Lets create first a method to calculate the rate 
# It takes two number a number to invest and a percentage of interest

def calculate_interstRate(saving, rate):
    return int(saving * (1 + rate / 100) ** 5)


def main():
    saving = int(input("Enter the number of saving: "))
    rate = int(input("Enter the percentages of interst: "))
    print(f'The value of your saving after 5 years is: {calculate_interstRate(saving, rate)}')

main() 