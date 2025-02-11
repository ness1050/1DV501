# Task to convert Seconds into the hour:minute:seconds

def convert(seconds):
    hours = seconds // 3600
    second = seconds % 3600
    minutes = second // 60
    final_seconds = second % 60
    return (f" {hours} Hours, {minutes} minutes, {final_seconds} seconds ")

def main():
    u1 = int(input("Enter number of seconds: "))
    print(f'This corrsponds to: {convert(u1)}')
    
main()
