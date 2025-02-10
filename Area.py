# Task to take input from users
# and calculate the Area of a circle 

# The mathemtical operation of Circle area
def circle_Area(radius):
    return round(((radius **2)*3.14),1)

def main():
    i = float(input("Enter the radius: "))
    print (f'The corresponding area is {circle_Area(i)}')
    
main()