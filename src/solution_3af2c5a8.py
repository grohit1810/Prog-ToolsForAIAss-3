# -*- coding: utf-8 -*-
"""Solution for Json 3af2c5a8

Run the file in the below format
python solution_3af2c5a8.py <path_to_file>
path_to_file -- ./JsonFiles/3af2c5a8.json

Created on Thu Nov 21 13:18:45 2019
@author: G Rohit, 19233292
"""

import sys 
from io_functions import arc_json_reader, print_grid

def solve_3af2c5a8(input):
    """Solver for input data of jason file 3af2c5a8.
    
    Solves the ARC task 3af2c5a8 as per perceived logic
    Arguments:
    input_data - python list of lists
    Output:
    output_data - python list of lists
    """ 
    #Reverse the input(list of list). The reverse performed is a row-wise reverse 
    #i.e. postion of each list in the list is reversed. 
    row_wise_reverse = input[::-1]
    #Reverse the input(list of list). The reverse performed is a column-wise reverse 
    #i.e. each list in the list is reversed
    column_wise_reverse = [row[::-1] for row in input]
    #Reverse the row-wise reversed input(list of list). The reverse performed is a column-wise reverse 
    column_wise_row_wise_reverse = [row[::-1] for row in row_wise_reverse]
    #use zip to combine the input with the three reverse list calculated above
    output = list(zip((input+column_wise_reverse),(row_wise_reverse+column_wise_row_wise_reverse)))
    #this done to convert tuple to list, as zip returns a tuple.
    output = [list(i+j) for i,j in output]
    return output

def solution_3af2c5a8_helper(file_path):
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
        output = solve_3af2c5a8(train_inputs[index])
        # Add the output from solver to output dictionary
        dict_output['TRAIN'+str(index)] = output
    # Loop the test data and send single grid of input to solver    
    for index in range(len(test_inputs)) : 
        output = solve_3af2c5a8(test_inputs[index])
        # Add the output from solver to output dictionary
        dict_output['TEST'+str(index)] = output
    return dict_output # Return the solved output grid

if __name__ == '__main__':
    
    # Check for input file, 
    # If number of arguments passed is not 2 -> print message and exit
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_3af2c5a8.py ./JsonFiles/3af2c5a8.json-- ")
        sys.exit()
    # Pass the file path from command-line argument to the variable
    file_path = sys.argv[1]
    output = solution_3af2c5a8_helper(file_path) # Call the helper function to solve json task
    print_grid(output) # Print the output of from helper function
    
