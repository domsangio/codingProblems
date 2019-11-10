# What is the largest prime factor of the number 600851475143 ?

# generate prime factorization list:

def generatePrimeFactorization(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return recurse(n / 2, [1, 2])
    else:
        return recurse(n, [1])

def recurse(n, primefactors):
    x = 3
    while x <= n:
        if x != 1 and n % x == 0:
            primefactors.append(x)
            return recurse(n / x, primefactors)
        x = x + 2
        
    return primefactors

pf = generatePrimeFactorization(600851475143)
print(pf[-1])
print(pf)

num = 1
for x in pf:
    num = num * x

print(num)
print(600851475143)
