# -*- coding: utf-8 -*-
"""Solution for Json 68b16354

Run the file in the below format
python solution_68b16354.py <path_to_file>
path_to_file -- ./JsonFiles/68b16354.json

Created on Sat Nov 16 20:28:52 2019
@author: G Rohit, 19233292
"""

import sys 
from io_functions import arc_json_reader, print_grid

#the input is python list of lists
def solve_68b16354(input):
    """Solver for input data of jason file 3af2c5a8.
    
    Solves the ARC task 3af2c5a8 as per perceived logic
    Arguments:
    input_data - python list of lists
    Output:
    output_data - python list of lists
    """ 

    #reverse the list and return
    return input[::-1]

    
def solution_68b16354_helper(file_path):
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
    train_inputs,train_outputs,test_inputs,test_outputs = arc_json_reader(sys.argv[1])
    # Initialize the output dictionary
    dict_output = {}
    # Loop the train data and send single grid of input to solver
    for index in range(len(train_inputs)) :
        output = solve_68b16354(train_inputs[index])
        # Add the output from solver to output dictionary
        dict_output['TRAIN'+str(index)] = output
    # Loop the test data and send single grid of input to solver    
    for index in range(len(test_inputs)) : 
        output = solve_68b16354(test_inputs[index])
        # Add the output from solver to output dictionary
        dict_output['TEST'+str(index)] = output
    return dict_output # Return the solved output grid

if __name__ == '__main__':
    
    # Check for input file, 
    # If number of arguments passed is not 2 -> print message and exit
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_68b16354.py ./JsonFiles/68b16354.json-- ")
        sys.exit()
    # Pass the file path from command-line argument to the variable
    file_path = sys.argv[1]
    output = solution_68b16354_helper(file_path) # Call the helper function to solve json task
    print_grid(output) # Print the output of from helper function
    