#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json
import numbers

"""
Load the geneated tensor data from the pickle file
"""

def load_tensor(files):
    for file in files:
        for line in open(file, 'r'):
            print(line)
            tensors = json.loads(line)
            print(tensors)


def main():
    files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature_tiny.txt.tensor.json',
             'data/noteevent-temperature/NOTEEVENTS_low_temperature_tiny.txt.tensor.json']

    # files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature.txt.tensor.json',
    #   'data/noteevent-temperature/NOTEEVENTS_low_temperature.txt.tensor.json']
    load_tensor(files)


if __name__ == "__main__":
    main()
