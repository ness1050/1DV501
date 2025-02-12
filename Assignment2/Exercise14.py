

def get_number(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d

def find_digits():
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(1, 10):
                    abcd = get_number(a, b, c, d)
                    dcba = get_number(d, c, b, a)
                    if dcba == 4 * abcd:
                        return a, b, c, d

if __name__ == "__main__":
    result = find_digits()
    if result:
        print(f"The digits are: A={result[0]}, B={result[1]}, C={result[2]}, D={result[3]}")
    else:
        print("No solution found.")