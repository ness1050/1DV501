
def convertFhToC(float):
    return (float - 32) / (9/5)    

def main():
    number = float(input("Enter a Fahrenheit number to convert to Celsius: "))
    
    print(f'The Farhenit in Celsuis:\t {convertFhToC(number)}')

main()