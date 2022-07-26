#!/usr/bin/python3

def all_possible(n=4):

    for i in range(n):
        matrix = []
        matrix.append([0, i])
        col = [z for z in range(n)]
        col.remove(i)
        recur_bt(matrix, 1, col, n)


def recur_bt(matrix, row, col, n):
   
    if len(matrix) is n:
        return matrix

    if row:
        i = row
        for j in col:
                if (not bot_right(matrix, i + 1, j + 1, n) or
                    not bot_left(matrix, i + 1, j - 1, n) or
                    not top_left(matrix, i - 1, j - 1, n) or
                        not top_right(matrix, i - 1, j + 1, n)):
                        continue
                matrix.append([i, j])
                new_col = list(col)
                new_col.remove(j)
                new_matrix = recur_bt(matrix, row + 1, new_col, n)
                if new_matrix is not None:
                    print(matrix)
                matrix.remove([i, j])
    return None


def bot_right(matrix, y, x, n):
    while y < n and x < n:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x += 1
    return True


def bot_left(matrix, y, x, n):
    while y < n and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x -= 1
    return True


def top_left(matrix, y, x, n):
    while y >= 0 and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x -= 1
    return True


def top_right(matrix, y, x, n):
    while y >= 0 and x < n:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x += 1
    return True

if __name__ == "__main__":
    from sys import argv
    if len(argv) is not 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    all_possible(n)
