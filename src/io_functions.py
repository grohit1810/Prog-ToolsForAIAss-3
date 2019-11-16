# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:44:21 2019

@author: 19233292
"""
import json
import pickle


def ARCTaskJsonReader(json_filename):
    json_file = open(json_filename)
    data = json.load(json_file)
    
    train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
    test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
    train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]
    
    return (train_inputs,train_outputs,test_inputs,test_outputs)