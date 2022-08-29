#!/usr/bin/env python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        fst_ind = 0
        sec_ind = 0
        for index in my_list:
            fst_ind += (index[0] * index[1])
            sec_ind += index[1]
        return (fst_ind / sec_ind)
    return 0
    