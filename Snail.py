'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

def snail(snail_map):
    x = 0
    y = 0
    x_max = len(snail_map[0])
    y_max = len(snail_map)
    x_min = -1
    y_min = -1
    total = (len(snail_map[0])) * (len(snail_map))
    out = []

    while True:

        while x != x_max :
            out.append(snail_map[y][x])
            x += 1
        x -= 1
        y += 1
        x_max -= 1

        if len(out) >= total:
            break

        while y != y_max :
            out.append(snail_map[y][x])
            y += 1
        y -= 1
        x -= 1
        y_max -= 1
        y_min += 1

        if len(out) >= total:
            break

        while x != x_min:
            out.append(snail_map[y][x])
            x -= 1
        x += 1
        y -= 1

        if len(out) >= total:
            break

        while y != y_min:
            out.append(snail_map[y][x])
            y -= 1
        x += 1
        y += 1
        x_min += 1

        if len(out) >= total:
            break

    return out