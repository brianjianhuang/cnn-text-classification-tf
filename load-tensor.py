#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json
import numbers
import numpy as np

"""
Load the geneated tensor data from the pickle file
"""

def load_tensor(files):
    tensors = []
    for file in files:
        for line in open(file, 'r'):
            print("line", line)
            tensors = tensors + [json.loads(line)]
            print("tensor", tensors)
    return tensors


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(len(data)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            print ("suffle_indices", shuffle_indices)
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]

def main():
    files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature_tiny.txt.tensor.json',
             'data/noteevent-temperature/NOTEEVENTS_low_temperature_tiny.txt.tensor.json']

    # files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature.txt.tensor.json',
    #   'data/noteevent-temperature/NOTEEVENTS_low_temperature.txt.tensor.json']
    tensors = load_tensor(files)
    iter = batch_iter(tensors, 1, 1)

    for batch in iter:
        print ("batch", batch)


if __name__ == "__main__":
    main()
