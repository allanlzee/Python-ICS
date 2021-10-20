nums = [] 

for i in range(1, 11): 
    nums.append(i) 

for i in range(len(nums)):
    if nums[i] % 2 == 0: 
        nums[i] *= -1

print(nums)