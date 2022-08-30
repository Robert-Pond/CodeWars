'''
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
'''

def spiralize(size):
    out = []
    cordyx = [0, size - 1]
    maxyx = [size - 1, size - 1]
    minyx = [0,0]
    data = []
    breaker = False

    for i in range(size):
        out.append([])
        for y in range(size):
            out[i].append(0)

    for i in range(size):
        out[0][i] = 1

    while True:

        data = down_left(out, cordyx, maxyx, minyx)
        out = data[0]
        cordyx = data[1]
        maxyx = data[2]
        minyx = data[3]
        breaker = data[4]
        
        if breaker:
            break
        if minyx[0] >= (size // 2) + 1 or minyx[1] >= (size // 2) + 1:
            break

        up_right(out, cordyx, maxyx, minyx)
        out = data[0]
        cordyx = data[1]
        maxyx = data[2]
        minyx = data[3]

        if minyx[0] >= (size // 2) + 1 or minyx[1] >= (size // 2) + 1:
            break


    
#     for i in out:
#         temp = ''
#         for y in i:
#             if y == 1:
#                 temp += '#'
#             else:
#                 temp += '.'
#         print(temp)

    return out

def down_left(spiral, curr, limit_high, limit_low):

    for y in range(curr[0], limit_high[0] + 1):  #down
        spiral[y][curr[1]] = 1
        curr[0] = y

    limit_high[0] -= 2
    curr[1] -= 1
    
    if curr[0] == (len(spiral) // 2) and curr[1] + 1 == (len(spiral) // 2) :
        return [spiral, curr, limit_high, limit_low, True]

    for x in range(curr[1], limit_low[1] - 1, -1):   #left
        spiral[curr[0]][x] = 1
        curr[1] = x

    limit_low[0] += 2
    limit_high[1] -= 2
    curr[0] -= 1

    # for i in spiral:
    #     print(i)
    # print()

    return [spiral, curr, limit_high, limit_low, False]

def up_right(spiral, curr, limit_high, limit_low):
    
    helper = 0
    if len(spiral) % 2 == 0:
        helper = 1

    for y in range(curr[0], limit_low[0] - 1, -1): #up
        spiral[y][curr[1]] = 1
        curr[0] = y

    curr[1] += 1
    limit_low[1] += 2

    if limit_low[0] + helper >= (len(spiral) // 2) + 1 or limit_low[1] + helper >= (len(spiral) // 2) + 1:
        return [spiral, curr, limit_high, limit_low]

    for x in range(curr[1], limit_high[1] + 1): #right
        spiral[curr[0]][x] = 1
        curr[1] = x
    #limit_low[0] += 1

    # for i in spiral:
    #     print(i)
    # print()
    return [spiral, curr, limit_high, limit_low]


#spiralize(9)


#first line of array done
#down left as func
#
# up right as func