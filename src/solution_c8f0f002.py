# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:48:54 2019

@author: 19233292
"""

import sys 
from io_functions import arc_task_json_reader
from output import print_grid

#the input is python list of lists
def solve_c8f0f002_json(input):
    
    input_copy = input.copy()
    for li in input_copy:
        for index_element in range(len(li)):
            if  li[index_element] == 7:
                li[index_element] = 5
    
    return input_copy

if __name__ == '__main__':
    
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_c8f0f002.py Path_to_c8f0f002.json-- ")
        sys.exit()

    train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
    print_dict = {}
    for index in range(len(train_inputs)) :
        output = solve_c8f0f002_json(train_inputs[index])
        print_dict['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_c8f0f002_json(test_inputs[index])
        print_dict['TEST'+str(index)] = output

    print_grid(print_dict)