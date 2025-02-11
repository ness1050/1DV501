#Write a program triangle.
# reading a positive odd integer n from the keyboard.
# and then prints two triangles. 
# First a right-angled triangle, then an isosceles triangle.


def printer(oddNumber):
    if oddNumber % 2 == 0:
        print("Please enter an odd number.")
        return


    # Right-angled triangle
    for i in range(oddNumber, 0, -1):
        space = oddNumber - i
        print(' ' * space + '*' * i )

    print()  # Blank line between the two triangles

    # Isosceles triangle
    for i in range(1, oddNumber + 1, 2):
        spaces = (oddNumber - i) // 2
        print(' ' * spaces + '*' * i + ' ' * spaces)
    
def main():
    user = int(input("Enter an odd number: "))
    printer(user)
    
main()
