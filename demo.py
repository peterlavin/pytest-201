'''
Created on 15 Sep 2020

@author: peter
'''
import json

class DemoError(Exception):
    pass


def add(a,b):
    if a == 99:
        raise DemoError()
    return a + b

def read_json(some_file_path):
    with open(some_file_path, 'r') as f:
        return json.load(f)