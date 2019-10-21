# Ideally I will be able to solve the subset sum problem

# Two implementations: solving it first, and solving every way
nums = input("Enter a list (comma separated) of numbers please: ")
target = input("Enter in a target number: ")

nums = nums.split(',')
nums = map(lambda x: int(x), nums)
nums = list(nums)

target = int(target)

print("List of numbers: " + str(nums))
print("Target number: " + str(target))

# Exhaustive search for all combinations of outcomes in order
# To find all sets of sums

answers = []

def find_subset(nums, currNums, target):
    if len(nums) == 0:
        return

    if (nums[0] + sum(currNums, 0) == target):
        new_list = list(currNums)
        new_list.append(nums[0])
        answers.append(new_list)
    
    if len(nums) > 0:
        list1 = currNums
        list2 = currNums.copy()
        list2.append(nums[0])
        find_subset(nums[1 : len(nums)], list1, target)
        find_subset(nums[1 : len(nums)], list2, target)

find_subset(nums, [], target)
print(answers)



