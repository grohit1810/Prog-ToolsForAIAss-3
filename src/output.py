# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 04:23:26 2019

@author: Mani Vegupatti
"""

import pickle



def print_grid(output):
    for key in output:
        for grid in (output[key]):
            for element in grid:
                print(element, end=" ")
            print("\n")
        print("----\n")
        

d = pickle.load(open("output_format.pkl","rb"))
print_grid(d)        