"""
DESCRIPTION:
Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

All inputs will be valid.
"""

def last(s):
    words = s[::-1].split()
    sortChars = []
    out = []
    finOut = []
    
    for i in words:
        sortChars.append(i[0])
        
    sortChars.sort()
    words.reverse()
    
    for x in sortChars:
        for y in words:
            if x == y[0]:
                out.append(y)
                words.pop(words.index(y))
                break
                
    for i in out:
        finOut.append(i[::-1])
        
    return finOut