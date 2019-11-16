# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:15:56 2019

@author: Mani Vegupatti
"""

from io_functions import arc_task_json_reader
from output import print_grid

json_filename = "./JsonFiles/08ed6ac7.json"

train_inputs,train_outputs,test_inputs,test_outputs = arc_task_json_reader(json_filename)
#print(train_inputs,"\n\n",train_outputs,"\n\n",test_inputs,"\n\n",test_outputs)

#print("Test_input",test_inputs[0])

#print("Test_output",test_outputs[0])


print_dict = {}
print_dict['test1'] = test_inputs[0]

print_dict['test2'] = test_outputs[0]

print_grid(print_dict)

print_dict['test1'] = train_inputs[0]
print_dict['test2'] = train_outputs[0]

print_grid(print_dict)