'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''


def solution(string,markers):
    common_break = string
    for i in markers:
        common_break = common_break.replace(i, '|')
    
    lines = common_break.split('\n')
    out = []
    
    for y in lines:
        if '|' in y:
            out.append(y.split('|')[0].strip())
        else:
            out.append(y.strip())
        
    return '\n'.join(out)
    

    
#     lines = string.split('\n')
#     print(lines)
#     new_code = []
#     to_do = []
    
#     if markers == []:
#         return string
    
#     for x in range(len(lines)):
#         to_do.append(' ')
        
#     for y in range(len(lines)):
#         for i in markers:
#             if i in lines[y]:
#                 to_do[y] = markers.index(i)
#             elif type(to_do[y]) != int:
#                 to_do[y] = -1
    
#     for z in range(len(to_do)):
#         if to_do[z] == -1:
#             new_code.append(lines[z])
#         else:
#             new_code.append(lines[z].split(markers[to_do[z]])[0].strip(' #'))
               
#     print(markers)
#     print(new_code)
#     return '\n'.join(new_code)