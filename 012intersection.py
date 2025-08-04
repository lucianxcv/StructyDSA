def intersection(a, b):
    set_b = set(b)
    intersected = []
    for number in a:
        if number in set_b:
            intersected.append(number)

    return intersected



print(intersection([4,2,1,6], [3,6,9,2,10]))
print(intersection([4,2,1], [1,2,4,6]))

"""
It converts list b into a set called set_b to speed up the lookup process.

It creates an empty list called intersected to store common numbers.

It goes through each number in list a.

For each number, it checks if that number is in set_b.

If yes, it adds the number to the intersected list.

After checking all numbers, it returns the intersected list containing all numbers from a that are also in b.
"""