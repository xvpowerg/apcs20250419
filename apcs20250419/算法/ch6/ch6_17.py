import random

nums = random.sample(range(1,100), 10)
print(nums)
nSum3 = 0
for i in range(3):
    maxNum = 0
    for k in range(len(nums)):
        if nums[k] > maxNum:
            maxNum = nums[k]
    nSum3 += maxNum
    nums.remove(maxNum)
print("最大3各數字和為:",nSum3)

