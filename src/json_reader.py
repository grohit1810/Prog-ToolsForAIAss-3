# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:02:38 2019

@author: 19233292
"""

import json
import pickle

json_file = open("c8f0f002.json")
data = json.load(json_file)
#print(data['train'][0]['output'])
'''
d = {}
d["train1"] = data['train'][0]['output']
d["train2"] = data['train'][2]['output']
d["train3"] = data['train'][0]['output']
d["test1"] = data['test'][0]['output']

pickle.dump( d, open( "output_format.pkl", "wb" ) )'''

train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]



def ARCTaskJsonReader(json_filename):
    json_file = open(json_filename)
    data = json.load(json_file)
    
    train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
    test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
    train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]
    
    return (train_inputs,train_outputs,test_inputs,test_outputs)