#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_new_matrix = matrix.copy()
    for each_line in range(len(matrix)):
        my_new_matrix[each_line] = list(map()lambda x : x**2), matrix[each_line]))
    return my_new_matrix
