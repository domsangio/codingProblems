# pythagorean triple that a + b + c = 1000

def findNums():
    for a in range (1, 998):
        for b in range(1, 1000 - a - 1):
            c = 1000 - a - b
            if a * a + b * b == c * c and a + b + c == 1000:
                        print(a)
                        print(b)
                        print(c)
                        print(a*b*c)
                        return

findNums()