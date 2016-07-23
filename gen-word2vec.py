#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json

"""
Generate a word to vec dictionary and dump to a json file

"""
def gen_word_list(files):
        all_words = list()
        for file in files:
                words =[ remove_number (word) for line in open(file, 'r') for word in clean_str(line).split()]
                all_words = all_words + words
        all_words = all_words + ["padding"]
        return list(set(all_words))

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = string.strip().lower()
    return string

def remove_number(s):
    """change any number to word number. """
    #print ("is number " + s)
    try:
        float(s)
        return "number"
    except ValueError:
        try:
            int(s)
            return "number"
        except ValueError:
            return s

def gen_vocabulary(all_words, output_file):
        """ generate the vocabulary lookup """
        word2vec = dict()
        for word in all_words:
                word2vec[word] = [random.random() for r in range(16)]
        #print (word2vec)
        json.dump(word2vec, open(output_file, "w"))

def main():
        #files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature_tiny.txt',
        #     'data/noteevent-temperature/NOTEEVENTS_low_temperature_tiny.txt']

        files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature.txt',
                 'data/noteevent-temperature/NOTEEVENTS_low_temperature.txt']
        output_file = "data/noteevent-temperature/word2vec_dict.json"
        all_words = gen_word_list(files)
        #print ("all_words", all_words)
        gen_vocabulary(all_words, output_file)
        print ("generate output file " + output_file)

if __name__ == "__main__":
        main()

