from random import randrange, choice

"""
    key: 5 by 5 matrix
    new_key: 5 by 5 matrix
"""

def swap_rows(key):
    row1 = randrange(5)
    row2 = choice([x for x in list(range(5)) if x != row1])
    temp_row = key[row1]
    key[row1] = key[row2]
    key[row2] = temp_row
    return key

def swap_columns(key):
    col1 = randrange(5)
    col2 = choice([x for x in list(range(5)) if x != col1])
    for row in range(5):
        temp = key[row][col1]
        key[row][col1] = key[row][col2]
        key[row][col2] = temp
    return key

def reverse(key):
    new_key = []
    for i in range(0, 5):
        new_key.append(key[4-i][::-1])
    key = new_key
    return key

def swap_two_letters(key):
    x1, x2, y1, y2 = randrange(5), randrange(5), randrange(5), randrange(5)
    temp = key[x1][y1]
    key[x1][y1] = key[x2][y2]
    key[x2][y2] = temp
    return key

def modify_key(key):
    type = randrange(50)
    if type == 0:
        return swap_rows(key)
    elif type == 1:
        return swap_columns(key)
    elif type == 2:
        return reverse(key)
    else:
        return swap_two_letters(key)


# TABLE = [
#     ['A', 'B', 'C', 'D', 'E'],
#     ['F', 'G', 'H', 'I', 'K'],
#     ['L', 'M', 'N', 'O', 'P'],
#     ['Q', 'R', 'S', 'T', 'U'],
#     ['V', 'W', 'X', 'Y', 'Z']
# ]

# print([row[1] for row in TABLE])
# swap_two_letters(TABLE)

# print(TABLE[0][::-1])

# print(modify_key(TABLE))