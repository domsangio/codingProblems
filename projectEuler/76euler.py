ways = {0: 0,1:0}


def setWays(n):
    sum = 0
    
    for i in range(1, n):
        sum += 1 + ways[i]

    ways[n] = sum

for i in range(2, 100):
    setWays(i)

for i in range (1, 100):
    print(i)
    print(ways[i])