#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json
import numbers

"""
Generate line to tensor and dump to pickle file
"""
def gen_text_tensor(files, word2vec, max_words):

    word_vec_size = len( word2vec["padding"])
    for file in files:
        out_file_name = file + ".tensor.json"
        print ("out put file " + out_file_name)
        if (os.path.isfile(out_file_name)):
            os.remove(out_file_name)
        out_file = open(out_file_name, "a")
        for line in open(file, 'r'):
            print ("line:" , line)
            words = line.lower().split()
            #print ("len word" , len(words))
            if (len(words) == 0):
                continue
            if (len(words) < max_words):
                words = pad_words(words, max_words)
            line_tensor = []
            for word in words:
                line_tensor.append(find_word_vec(word, word2vec, word_vec_size))
            print("line tensor :" , line_tensor)
            json.dump(line_tensor, out_file)
            out_file.write("\n")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        try:
            int(s)
            return True
        except:
            return False

def find_word_vec(word, word2vec, word_vec_size):
    if (is_number(word)):
        number_tensor = [0.0] * word_vec_size
        #just ot normlize the number a bit
        norm_number = 1 -  10 / (float(word) + 1)
        number_tensor[0] = norm_number
        return number_tensor
    else:
        padding_vec = word2vec.get("padding")
        return word2vec.get(word, padding_vec)

def pad_words(words, length):
    """
    Appends "a" to list to get length of list equal to `length`.
    """
    diff_len = length - len(words)
    if diff_len <= 0:
        return words
    return words  + ["padding"] * diff_len

def find_max_words(files):
    """
    Find the longest line, need to pad the shorter ones
    """
    all_num_words = list()
    for file in files:
        num_words =[len(line.split()) for line in open(file, 'r')]
        all_num_words = all_num_words + num_words
    #print (all_num_words)
    return max(all_num_words)

def load_word2vec(word2vec_json_file):
    """ generate the vocabulary lookup """
    word2vec = json.load(open(word2vec_json_file, "r"))
    print ("padding " + str(word2vec["padding"][0]))
    return word2vec

def main():
     files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature_small.txt',
         'data/noteevent-temperature/NOTEEVENTS_low_temperature_small.txt']

     #files = ['data/noteevent-temperature/NOTEEVENTS_high_temperature.txt',
     #   'data/noteevent-temperature/NOTEEVENTS_low_temperature.txt']

     word2vec_file = "data/noteevent-temperature/word2vec_dict.json"
     word2vec = load_word2vec(word2vec_file)
     max_words = find_max_words(files)
     gen_text_tensor(files, word2vec, max_words)
     #print ("generate output file " + output_file)

if __name__ == "__main__":
    main()

