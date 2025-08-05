def five_sort(nums):
    i = 0  # Start pointer from the beginning of the list
    j = len(nums) - 1  # Start pointer from the end of the list

    while i <= j:  # Loop until the two pointers meet or cross
        if nums[j] == 5:  # If the element at the end is already 5
            j -= 1  # Move the end pointer left
        elif nums[i] == 5:  # If the element at the start is 5
            nums[i], nums[j] = nums[j], nums[i]  # Swap it with the element at the end
            i += 1  # Move the start pointer right
        else:
            i += 1  # If nums[i] is not 5, just move forward

    return nums  # Return the modified list

print(five_sort([12, 5, 1, 5, 12, 7]))