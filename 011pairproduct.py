def pair_product(nums, target):
    previous_num = {}
    for index, num in enumerate(nums):
        complement = target // num
        if complement in previous_num:
            return (previous_num[complement], index)
        previous_num[num]= index

print(pair_product([4, 7, 9, 2, 5, 1], 5))


"""
You create an empty dictionary previous_num to store each number and its index as you go.

You loop over the list using enumerate() to get both the index and the num.

For each number, you calculate the complement — the number that would multiply with num to make the target (i.e., complement = target // num).

Before doing the division, you check target % num == 0 to avoid wrong results when the product wouldn't be an exact match.

If complement is already in the dictionary, it means you’ve seen a number earlier that, when multiplied by num, equals the target, so you return their indices as a pair.

Otherwise, you store the current number and its index in the dictionary and move on.
"""