# Inside file distance
# create a function distance(x1,y1,x2,y2) 
# which computes the distance between two points x1,y1 and x2,y2

def function():
    x1 = float(input("Enter first x1 coordinate number: "))
    y1 = float(input("Enter first y1 coordinate number: "))
    x2 = float(input("Enter first x2 coordinate number: "))
    y2 = float(input("Enter first y2 coordinate number: "))
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2 )
    print(f'Distance between coordinate {x1, x2, y1, y2} is {round(distance, 3)}')
    return distance

def sqrt(n):
    return n**0.5

def main():
    function()
    
main()