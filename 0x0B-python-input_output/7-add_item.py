#!/usr/bin/python3
'''Module for task 7'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file'''
    with open(filename, 'w') as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
