# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#  find the sum of the even-valued terms.

# generate fibonacci numbers
fibList = [1]

prev1 = 1
prev2 = 1

def genFib(prev1, prev2):
    currFib = prev1 + prev2
    if currFib < 4000000:
        fibList.append(currFib)
        prev2 = prev1
        prev1 = currFib
        genFib(int(currFib), int(prev2))

sum = 0

genFib(1, 1)

for x in fibList:
    if x % 2 == 0:
        sum += x
        print("EVEN")
    print(x)

print(sum)

