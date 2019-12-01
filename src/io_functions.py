# -*- coding: utf-8 -*-
"""Input/Ouput functions for ARC task.

It contains 2 functions arc_json_reader and print_grid

Function print_grid will print the output of the solver to terminal
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

Created on Sat Nov 16 18:44:21 2019
@author: 19233292, G Rohit
@author: 19232668, Mani Vegupatti
"""

import json

def arc_json_reader(json_filename):
    """Reader function to read and parse ARC task Json file."""
    json_file = open(json_filename)
    data = json.load(json_file)
    
    train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
    test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
    train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]
    
    return (train_inputs,train_outputs,test_inputs,test_outputs)

def print_grid(output):
    """Print function to print the ARC task output of solver to console."""
    for key in output: # Get the grid
        for row in (output[key]):# Get the row
            for element in row: 
                print(element, end=" ")  # Print element, stay in same line
            print()
        print()
        
if __name__ == "__main__":
    
    #import doctest and test
    import doctest
    doctest.testmod()
    
