def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0 #bases for which we will keep incrementing

        count[char] += 1

    biggest = None
    for char in s:
        if biggest is None or count[char] > count[biggest]:
            biggest = char

    return biggest

"""
Define the function
You define a function called most_frequent_char that takes a string s as input.

Create an empty dictionary
You initialize a dictionary called count to store how many times each character appears in the string.

Loop through each character in the string
For every character in s:

If the character is not already in the count dictionary, you add it with a value of 0.

Then, you increment its value by 1.
This builds a frequency map — a dictionary where the keys are characters and the values 
are how many times they appear in the string.

Initialize the biggest variable
You set a variable biggest = None. This will eventually hold the character that appears the most in the string.

Loop through the string again
For every character in s (in order):

If biggest is still None (i.e. first loop), 
or if the current character has a higher count than the character stored in biggest, 
then update biggest to the current character.

Return the result
After the loop finishes, the variable biggest contains the most frequent character in the string. So you return it.

Example:
If the input is "banana", then:

b occurs 1 time

a occurs 3 times

n occurs 2 times

So the function returns 'a', because it's the character with the highest frequency.


"""



