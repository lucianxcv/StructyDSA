def max_value(nums):
    max = float('-inf')
    for num in nums:
        if num > max:
            max = num

    return max

nums = [2,3,5,1,100,1,101]
print(max_value(nums))

#n = length of list
#Time: O(n)
#Space: O(1)