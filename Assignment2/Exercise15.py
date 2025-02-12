import random
import math

# Assume a unit circle centred around origin inside a square with sides
# 2 like in the figure above.
# Assume also that we randomly generate N points (x,y)
# where both x and y are within the range [- 1,1]. 
# The proportion of points inside the circle should
# then approximately be the same as the ratio between the circle area 
# pi*R*R (which equals pi since R=1) and the square area 4. 
# This relation can be used to compute an approximation of pi.
# Write a program pi_approx.py that computes (and prints) a pi approximation for N=100, N=10000, and N=1000000.
# Print also the error (i.e. the absolut value of pi_actual - pi_approx)

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_approx = (inside_circle / num_points) * 4
    return pi_approx

def main():
    actual_pi = math.pi
    for N in [100, 10000, 1000000]:
        pi_approx = estimate_pi(N)
        error = abs(actual_pi - pi_approx)
        print(f'N={N}: pi_approx={pi_approx}, error={error}')

if __name__ == "__main__":
    main()