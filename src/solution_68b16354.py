# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:28:52 2019

@author: 19233292
"""

import sys 
from io_functions import arc_task_json_reader
from output import print_grid

#the input is python list of lists
def solve_68b16354_json(input):
    return input[::-1]

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_68b16354.py Path_to_68b16354.json-- ")
        sys.exit()

    train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
    print_dict = {}
    for index in range(len(train_inputs)) :
        output = solve_68b16354_json(train_inputs[index])
        print_dict['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_68b16354_json(test_inputs[index])
        print_dict['TEST'+str(index)] = output

    print_grid(print_dict)
    
