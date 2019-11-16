# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 04:23:26 2019

@author: Mani Vegupatti

This will print the output of the solver to terminal
>>> dict_data = { "TRAIN1": [[1, 8, 8, 5, 5, 8], [1, 1, 5, 5, 1, 8], [5, 1, 1, 5, 5, 8]], "TRAIN2": [[1, 8, 1, 5, 1, 2], [5, 8, 8, 1, 1, 3], [5, 1, 8, 8, 5, 5]], "TEST1": [[2, 5, 6, 5, 3, 1], [4, 3, 2, 6, 9, 5], [1, 3, 5, 7, 9, 4]] }
>>> print_grid(dict_data)
1 8 8 5 5 8 
1 1 5 5 1 8 
5 1 1 5 5 8 
<BLANKLINE>
1 8 1 5 1 2 
5 8 8 1 1 3 
5 1 8 8 5 5 
<BLANKLINE>
2 5 6 5 3 1 
4 3 2 6 9 5 
1 3 5 7 9 4 
<BLANKLINE>

Sample from pickle 
d = pickle.load(open("output_format.pkl","rb"))
print_grid(d)        
"""



def print_grid(output):
    for key in output:
        for grid in (output[key]):
            for element in grid:
                print(element, end=" ")
            print("")
        print("")
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
