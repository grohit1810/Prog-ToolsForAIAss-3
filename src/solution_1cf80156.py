# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:15:56 2019
@author: Mani Vegupatti


"""
import sys 
from io_functions import arc_task_json_reader, print_grid
import numpy as np

#the input numpy nd-array
def solve_1cf80156(input_data):
    row_arr= np.all(input_data==0, axis=1)
    row_arr_index = np.where(row_arr == False)
    col_arr = np.all(input_data==0, axis=0)
    col_arr_index = np.where(col_arr == False)
    output_data = input_data[row_arr_index[0][0]:row_arr_index[0][-1]+1,
                             col_arr_index[0][0]:col_arr_index[0][-1]+1]
    return output_data

def workflow(file_path):
    train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
    dict_output = {}
    for index in range(len(train_inputs)) :
        output = solve_1cf80156(np.array(train_inputs[index]))
        dict_output['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_1cf80156(np.array(test_inputs[index]))
        dict_output['TEST'+str(index)] = output
    return dict_output

if __name__ == '__main__':

    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_1cf80156.py ./JsonFiles/1cf80156.json-- ")
        sys.exit()
    
    file_path = sys.argv[1]
    output = workflow(file_path)
    print_grid(output)
