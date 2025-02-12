# Write a program largest_k
# which for any given positive integer n (read from the keyboard) 
# computes the largest integer k such that 0+2+4+6+8+...+k < n. 


def largestK(number):
	k = 0
	sum_even = 0
	while sum_even + k < number:
		sum_even += k
		k += 2
	return k - 2

    
def main():
    Ui = int(input("Enter a Full number: "))
    print(largestK(Ui))

main()