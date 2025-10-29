x = int(input("enetr a number :"))

nums = (1,35,6,78,25,36)
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx" , i)
        i += 1
