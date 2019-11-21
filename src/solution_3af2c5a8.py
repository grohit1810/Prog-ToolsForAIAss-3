# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:18:45 2019

@author: 19233292
"""

import sys 
from io_functions import arc_task_json_reader
from output import print_grid

#the input is python list of lists
def solve_3af2c5a8_json(input):
    #actual+column_wise_reverse
    #row_wise_reverse+
    row_wise_reverse = input[::-1]
    column_wise_reverse = [row[::-1] for row in input]
    column_wise_row_wise_reverse = [row[::-1] for row in row_wise_reverse]
    output = list(zip((input+column_wise_reverse),(row_wise_reverse+column_wise_row_wise_reverse)))
    return output
if __name__ == '__main__':
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_3af2c5a8.py Path_to_3af2c5a8.json-- ")
        sys.exit()

    train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
    print_dict = {}
    for index in range(len(train_inputs)) :
        output = solve_3af2c5a8_json(train_inputs[index])
        #print_dict['TRAIN'+str(index)] = output
        print_dict['TRAIN1'+str(index)] = train_inputs[index]
        print_dict['TRAIN2'+str(index)] = train_outputs[index]
    for index in range(len(test_inputs)) : 
        output = solve_3af2c5a8_json(test_inputs[index])
        #print_dict['TEST'+str(index)] = output
        print_dict['TRAIN11'+str(index)] = test_inputs[index]
        print_dict['TRAIN22'+str(index)] = test_outputs[index]

    print_grid(print_dict)
    
