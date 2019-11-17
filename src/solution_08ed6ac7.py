# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:15:56 2019

@author: Mani Vegupatti
"""

import sys 
from io_functions import arc_task_json_reader, print_grid
import numpy as np


#json_filename = "./JsonFiles/08ed6ac7.json"

#the input is python list of lists
def solve_08ed6ac7_json(input):
    colour = 1
    input_np = np.array(input)
    #print(input_copy.shape)
    rows = input_np.shape[0]
    columns = input_np.shape[1]
    for x in range(0,rows):
        for y in range(0,columns):
            if  input_np[x][y] == 5:
                #print(x, y, rows, columns)
                #print(input_np[x:rows,y])
                input_np[x:rows,y] = colour
                colour += 1
    return input_np

if __name__ == '__main__':
    
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_08ed6ac7.py Path_to_08ed6ac7.json-- ")
        sys.exit("Exit - Bad File")
train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(sys.argv[1])
#train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(json_filename)
print_dict = {}
for index in range(len(train_inputs)) :
    output = solve_08ed6ac7_json(train_inputs[index])
    print_dict['TRAIN'+str(index)] = output
    for index in range(len(test_inputs)) : 
        output = solve_08ed6ac7_json(test_inputs[index])
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