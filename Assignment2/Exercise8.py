# Write a program random_numbers that reads a positive integer n from the keyboard and then:
# Generates and prints (in a single line) n random numbers in the interval [1,100]
# Prints the average value (with two decimals), the smallest number (min), and the largest number (max).

from random import randint

# Read a positive integer n from the keyboard
n=int(input("enter a postive digit to be generated:"))

sum = 0
max = 0
min = 101
for i in range(n):
        if n > 0 and n !=0:
                random_number = randint(1, 100)
                sum += random_number
        if max < random_number:
                max = random_number
        if min > random_number:
                min = random_number
        print(random_number, end= " ")
print(f'\nmax: {max}\nand min is: {min}\naverage: {round((sum/n), 1)}\n')

