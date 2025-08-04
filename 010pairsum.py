def pair_sum(numbers, target):
    previous_nums = {}
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in previous_nums:
            return(previous_nums[complement], index)
        previous_nums[num] = index


print(pair_sum([3, 2, 5, 4, 1], 8))



"""
You start by creating an empty dictionary called previous_nums. 
This will keep track of numbers you’ve already seen in the list and the index where each one appeared.

Next, you loop through the list called numbers, and on each loop you get both the index of the element and the number itself.

Inside the loop, you calculate something called complement, 
which is the number you need to add to the current number to reach the target. 
For example, if the target is 10 and the current number is 4, then the complement is 6.

Then you check if that complement is already in the dictionary. 
If it is, it means you’ve already seen a number earlier in the list that can pair with the current number to make the target. 
In that case, you immediately return a pair of indices — the index of the complement (from the dictionary) and the index of the current number.

If the complement isn’t in the dictionary, you store the current number and its index in the dictionary, so it can be used for future checks.


"""