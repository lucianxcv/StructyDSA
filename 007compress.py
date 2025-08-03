def compress(s):
    s += '!'
    result = ''
    i = 0
    j = 0
    while j <len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result += s[i]
            else:
                result += str(num) +s[i]

            i = j
    return result

print(compress('ssssbbz'))

"""
Appends a sentinel character '!' to avoid index errors and simplify edge handling.

i marks the start of a group of repeated characters.

j advances while characters are the same.

Once a different char is found:

It calculates how many times the char at i occurred: j - i

If 1, just appends the character.

If more than 1, appends the count and the character.

Then sets i = j and repeats.
---------------------------------------------------------
. Use a list for better performance, just like with uncompress:
python
Copy
Edit
def compress(s):
    s += '!'  # sentinel
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num) + s[i])
            i = j
    return ''.join(result)


"""