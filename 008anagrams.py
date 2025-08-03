def anagrams(s1,s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count

print(anagrams('restful', 'fluster'))


"""
def anagrams(s1, s2):
Defines a function named anagrams that takes two string arguments: s1 and s2.

return char_count(s1) == char_count(s2)
Calls char_count on both strings.

Compares the two resulting dictionaries.

Returns True if they are equal (i.e., the two strings have exactly the same letters with the same frequencies), otherwise returns False.

def char_count(s):
Defines a helper function that counts how many times each character appears in a given string s.

count = {}
Creates an empty dictionary named count to store the frequency of each character.

for char in s:
Loops through each character in the input string s.

if char not in count:
Checks if the current character hasn’t been seen yet (i.e., not yet in the dictionary).

count[char] = 0
If the character is new, it initializes its count to 0 (preparing to increment it in the next line).

count[char] += 1
Adds 1 to the current count of that character (whether it was just initialized or already present).

return count
After looping through the entire string, 
returns the count dictionary which contains each character as a key and its frequency as the value.
"""