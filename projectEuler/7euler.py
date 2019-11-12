# 10 001 prime

import math

def isPrime(n):
    for x in range(3, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True

numPrimes = 1
currPrime = 2

currNum = 3

while numPrimes != 10001:
    if isPrime(currNum):
        currPrime = currNum
        numPrimes = numPrimes + 1
        print(numPrimes)
        print(currPrime)


    currNum = currNum + 2

print(currPrime)