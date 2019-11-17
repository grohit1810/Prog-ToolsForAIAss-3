# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:15:56 2019

@author: Mani Vegupatti
"""

import sys 
from io_functions import arc_task_json_reader, print_grid
import numpy as np


#json_filename = "./JsonFiles/1cf80156.json"

#the input is python list of lists
def solve_1cf80156_json(input):
    #colour = 1
    input_np = np.array(input)
    #print(input_copy.shape)
    row_arr= np.all(input_np==0, axis=1)
    #print(row_arr)
    row_arr_index = np.where(row_arr == False)
    col_arr = np.all(input_np==0, axis=0)
    #print(col_arr)
    col_arr_index = np.where(col_arr == False)
    #print(row_arr_index[0][0] )
    input_np = input_np[row_arr_index[0][0]:row_arr_index[0][-1]+1,col_arr_index[0][0]:col_arr_index[0][-1]+1]
    #print(input_np)
    return input_np

if __name__ == '__main__':
    
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_1cf80156.py ./JsonFiles/1cf80156.json-- ")
        sys.exit("Exit - Bad File")
train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
#train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(json_filename)
print_dict = {}
for index in range(len(train_inputs)) :
    output = solve_1cf80156_json(train_inputs[index])
    print_dict['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_1cf80156_json(test_inputs[index])
        print_dict['TEST'+str(index)] = output

print_grid(print_dict)

"""train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(json_filename)
#print(train_inputs,"\n\n",train_outputs,"\n\n",test_inputs,"\n\n",test_outputs)

#print("Test_input",test_inputs[0])

#print("Test_output",test_outputs[0])
print_dict = {}
print_dict['test1'] = test_inputs[0]

print_dict['test2'] = test_outputs[0]

print_grid(print_dict)

print_dict['test1'] = train_inputs[0]
print_dict['test2'] = train_outputs[0]

print_grid(print_dict)"""