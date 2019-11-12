def isPalindrome(x):
    newNum = 0
    oldNum = x
    while oldNum > 0:
        newNum = newNum * 10 + oldNum % 10
        oldNum = oldNum / 10
        oldNum = int(oldNum)

    return newNum == x


maxPalindrome = 0

for x in range(100, 999):
    for y in range(100, 999):
        if isPalindrome(y * x):
            if y * x > maxPalindrome:
                maxPalindrome = x * y

print(maxPalindrome)