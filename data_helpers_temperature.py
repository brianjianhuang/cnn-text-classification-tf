import numpy as np
import re
import itertools
from collections import Counter
import json


def load_data_and_labels(positive_file, negative_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """


    # Load data from files
    positive_examples = list(open(positive_file, "r").readlines())
    positive_examples = [json.loads(s) for s in positive_examples]
    negative_examples = list(open(negative_file, "r").readlines())
    negative_examples = [json.loads(s) for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
  
    # Generate labels
    positive_labels = [[0.0, 1.0] for _ in positive_examples]
    negative_labels = [[1.0, 0.0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    #print ('x_text = ', x_text)
    #print (" y = " ,y )
    return [x_text, y]
   

def load_data():
    """
    Loads and preprocessed data for the MR dataset.
    Returns input vectors, labels, vocabulary, and inverse vocabulary.
    """
    print ('load date(), loading temperature data')

    #Train on the small data set to test it out
    #positive_file = "./data/noteevent-temperature/NOTEEVENTS_high_temperature_tiny.txt"
    #negative_file = "./data/noteevent-temperature/NOTEEVENTS_low_temperature_tiny.txt"
    positive_file = "./data/noteevent-temperature/NOTEEVENTS_high_temperature_small.txt.tensor.json"
    negative_file = "./data/noteevent-temperature/NOTEEVENTS_low_temperature_small.txt.tensor.json"
    # Load and preprocess data
    sentences, labels = load_data_and_labels(positive_file, negative_file)

    #print ("vocabulary inv")
    #print  (vocabulary_inv)

    x = sentences
    y = labels
    return [x, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    #print ("batch_iter input", data, batch_size)

    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(len(data)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]

def main():
    x, y = load_data()
    print ("x", x)
    print ("y", y)
    #batchs = batch_iter(list(zip(x, y)), 1, 1)

    for batch in batchs:
        print ("batch", batch)


if __name__ == "__main__":
    main()
