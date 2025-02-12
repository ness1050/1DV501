 # Write a program two_dice 
 # that use the random module to simulate that you are rolling two dice
 # 10000 times. At the same time
 # keep track of the number of times you get the result (adding the dice values) 2, 3, ..., 11, 12. (Use a list to store a count of the numbers.) After the simulation, present the frequencies for the different numbers. 
 # An example of an execution:

from random import randint

def Two_dice():
    return randint(1, 6)

result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10000):
    the_sum = Two_dice() + Two_dice()
    result_list[the_sum - 2] += 1

current = 2 

for i in result_list:
    print(f'{current}:   {i}')
    current +=1 
    

