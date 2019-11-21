# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:48:54 2019

@author: 19233292
"""

import sys 
from io_functions import arc_task_json_reader
from output import print_grid
import numpy as np

#the input is numpy nd array
def solve_c8f0f002_json(input):
    return(np.where(input!=7,input,5).tolist())

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_c8f0f002.py Path_to_c8f0f002.json-- ")
        sys.exit()

    train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
    print_dict = {}
    for index in range(len(train_inputs)) :
        output = solve_c8f0f002_json(np.array(train_inputs[index]))
        print_dict['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_c8f0f002_json(np.array(test_inputs[index]))
        print_dict['TEST'+str(index)] = output

    print_grid(print_dict)