# numbers 1 to 1000

# find the sum of all numbers divisible by 3 and 5 but not by 15

num3_max = 999 / 3
num3_min = 3 / 3

num5_max = 1000 / 5
num5_min = 5 / 5

num15_max = (1000 - 1000 % 15) / 15
print((str) (num15_max))
num15_min = 15 / 15

sum3 = 3.0 * ((float)(num3_max + num3_min))/2.0 * (num3_max - num3_min + 1)

print (sum3)


sum5 = 5.0 * ((float)(num5_max + num5_min))/2.0 * (num5_max - num5_min + 1)
sum15 = 15.0 * ((float)(num15_max + num15_min))/2.0 * (num15_max - num15_min + 1)

print ((str) (sum3 + sum5 - sum15 - 1000))  # fastest answer method

sum = 0

for x in range(1000):
    if x % 5 == 0 or x % 3 == 0:
        sum += x

sum3 = 334 / 2 * 333 * 3
sum5 = 5 * 201 * 100
sum15 = 33 * 67 * 15

print(sum3)
print(sum5)
print(sum15)
print(sum3 + sum5 - sum15 - 1000)

print(sum)