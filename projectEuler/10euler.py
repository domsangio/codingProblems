# sum of primes less than 1000000

import math

numbers = [2]

def isPrime(n):
    for x in range(3, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True

for x in range (3, 2000000, 2):
    if isPrime(x):
        numbers.append(x)

sum = 0
for x in numbers:
    sum += x

print(sum)