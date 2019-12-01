# -*- coding: utf-8 -*-
"""Solution for Json 1cf80156

Run the file in the below format
python solution_1cf80156.py <path_to_file>
path_to_file -- ./JsonFiles/1cf80156.json

Created on Sun Nov 17 01:15:56 2019
@author: Mani Vegupatti, 19232668
"""

import sys 
from io_functions import json_reader, print_grid
import numpy as np

def solve_1cf80156(input_data):
    """Solver for input data of jason file 1cf80156.
    
    Solves the ARC task 1cf80156 as per perceived logic
    Arguments:
    input_data - Numpy ND array of input data
    Output:
    output_data - Numpy ND array of solved output
    """ 
    
    # Get boolean array by checking value 0 across columns(axis=1)
    # We get rows with all Zeros as True
    row_arr= np.all(input_data==0, axis=1)
    # Get an array with index_number(of rows), where non-zero value exists
    row_arr_index = np.where(row_arr == False)
    # Get bollean array by checking value 0 across rows(axis=0)
    # We get columns with all Zeros as True
    col_arr = np.all(input_data==0, axis=0)
    # Get an array with index_number(of columns), where non-zero value exists
    col_arr_index = np.where(col_arr == False)
    # Form an output boundry using the row index and column index
    # Get the slice of output from input, using the boundary values
    output_data = input_data[row_arr_index[0][0]:row_arr_index[0][-1]+1,
                             col_arr_index[0][0]:col_arr_index[0][-1]+1]
    return output_data 

def workflow(file_path):
    """Defines the pipeline for task 1cf80156.
    
    Defines Pipeline for,
        1. Reading Input Data
        2. Sending single grid to solver
        3. Combining the ouput from solver for printing
    Reads the data from Jsonfile. 
    Loops the Train and Test input data  
    Sents single grid data to solver
    """
    
    # Read input data from json and split into train, test input and outputs
    train_inputs,train_outputs,test_inputs,test_outputs = json_reader(sys.argv[1])
    # Initialize the output dictionary
    dict_output = {}
    # Loop the train data and send single grid of input to solver
    for index in range(len(train_inputs)) :
        output = solve_1cf80156(np.array(train_inputs[index]))
        # Add the output from solver to output dictionary
        dict_output['TRAIN'+str(index)] = output
    # Loop the test data and send single grid of input to solver    
    for index in range(len(test_inputs)) : 
        output = solve_1cf80156(np.array(test_inputs[index]))
        # Add the output from solver to output dictionary
        dict_output['TEST'+str(index)] = output
    return dict_output # Return the solved output grid

if __name__ == '__main__':
    
    # Check for input file, 
    # If empty -> print message and exit
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_1cf80156.py ./JsonFiles/1cf80156.json-- ")
        sys.exit()
    # Pass the file path from command-line argument to the variable
    file_path = sys.argv[1]
    output = workflow(file_path) # Call the worflow to solver
    print_grid(output) # Print the output of solver
