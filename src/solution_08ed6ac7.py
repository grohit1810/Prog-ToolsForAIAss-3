# -*- coding: utf-8 -*-
"""Solution for Json 08ed6ac7

Run the file in the below format
python solution_08ed6ac7.py <path_to_file>
path_to_file -- ./JsonFiles/08ed6ac7.json

Created on Sun Nov 17 01:15:56 2019
@author: Mani Vegupatti, 19232668
"""

import sys 
from io_functions import json_reader, print_grid
import numpy as np

def solve_08ed6ac7(input_data):
    """Solver for input data of jason file 08ed6ac7.
    
    Solves the ARC task as per perceived logic
    Arguments:
    input_data - Numpy ND array of input data
    Output:
    output_data - Numpy ND array of solved output
    """ 
    
    colour = 1 # Set Initial colour as blue = 1
    rows = input_data.shape[0] # Get number of rows of input matrix
    columns = input_data.shape[1] # Get number of Columns of input matrix
    output_data = np.copy(input_data) # Copy input to output
    # Loop the input matrix 
    for x in range(0,rows):
        for y in range(0,columns):
            # Look for colour grey = 5
            if  output_data[x][y] == 5:
                # Replace current column with current color
                # The Rows to be filled are current row till end of all rows
                output_data[x:rows,y] = colour
                colour += 1 # Increment the colour
    return output_data

def workflow(file_path):
    """Defines the pipeline for task 08ed6ac7.
    
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
        output = solve_08ed6ac7(np.array(train_inputs[index]))
        # Add the output from solver to output dictionary
        dict_output['TRAIN'+str(index)] = output
    # Loop the test data and send single grid of input to solver
    for index in range(len(test_inputs)) : 
        output = solve_08ed6ac7(np.array(test_inputs[index]))
        # Add the output from solver to output dictionary
        dict_output['TEST'+str(index)] = output
    return dict_output # Return the solved output grid

if __name__ == '__main__':

    # Check for input file, 
    # If empty -> print message and exit
    if len(sys.argv) != 2 :
        print("Please run the file in this format. --python solution_08ed6ac7.py ./JsonFiles/08ed6ac7.json-- ")
        sys.exit()
    # Pass the file path from command-line argument to the variable
    file_path = sys.argv[1]
    output = workflow(file_path) # Call the worflow to solver
    print_grid(output) # Print the output of solver
