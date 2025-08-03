def uncompress(s):
    numbers = '0123456789'
    result = ''
    i = 0
    j = 0
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result += s[j] * num
            j += 1
            i = j

    return result

print(uncompress("2c3a1t"))

"""How it works step-by-step:
Input: "2c3a1t"

Start with i = 0 and j = 0.

Move j forward while s[j] is a digit → until j = 1, s[j] = 'c'.

Convert s[i:j] (i.e., '2') to num = 2, then result += 'c' * 2 → 'cc'.

Move j to next position, and set i = j → continue from i = 2.

Repeat this for:

'3a' → 'aaa'

'1t' → 't'

------------------------------------------------------------------------------------------
Your current code does:

result += s[j] * num
Since strings in Python are immutable, this operation creates a new string every time
 — which is inefficient, especially with many or large repeated characters. 
 The time complexity becomes O(n²) in the worst case because each += operation may copy the whole string again.

------------------------------------------------------------------------------------------
def uncompress(s):
    numbers = '0123456789'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j
    return ''.join(result)

print(uncompress("2c3a1t"))
====================================================================
Benefits:
Now the time complexity is O(n), where n is the total length of the final string.

Memory usage is also better managed.

✅ This version is much more efficient and scalable for large inputs. Good optimization

"""