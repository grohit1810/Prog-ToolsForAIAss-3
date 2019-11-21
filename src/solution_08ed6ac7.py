# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:15:56 2019

@author: Mani Vegupatti
"""

import sys 
from io_functions import arc_task_json_reader, print_grid
import numpy as np

#the input numpy nd-array
def solve_08ed6ac7(input_data):
    colour = 1
    rows = input_data.shape[0]
    columns = input_data.shape[1]
    output_data = np.copy(input_data)
    for x in range(0,rows):
        for y in range(0,columns):
            if  output_data[x][y] == 5:
                output_data[x:rows,y] = colour
                colour += 1
    return output_data

def workflow(file_path):
    train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
    dict_output = {}
    for index in range(len(train_inputs)) :
        output = solve_08ed6ac7(np.array(train_inputs[index]))
        dict_output['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_08ed6ac7(np.array(test_inputs[index]))
        dict_output['TEST'+str(index)] = output
    return dict_output

if __name__ == '__main__':

    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_08ed6ac7.py ./JsonFiles/08ed6ac7.json-- ")
        sys.exit()
    
    file_path = sys.argv[1]
    output = workflow(file_path)
    print_grid(output)
