"""
DESCRIPTION:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', "u"]
    out = 0
    for i in vowels:
        out += sentence.count(i)
    return out

        
def get_count1(sentence):
    vowels = ['a', 'e', 'i', 'o', "u"]
    out = 0
    for i in list(sentence):
        if i in vowels:
            out += 1
    return out