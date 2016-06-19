#!/usr/bin/python

import re
import os
import sys


noteevent_file_path = "C:/Users/Brian/workspace/nlp/NOTEEVENTS.csv"

script_dir = os.path.dirname(os.path.abspath(__file__))

temperature_file_high_path = script_dir + "/data/noteevent-temperature/NOTEEVENTS_high_temperature.txt"
temperature_file_low_path = script_dir + "/data/noteevent-temperature/NOTEEVENTS_low_temperature.txt"


temperature_file_high = open ( temperature_file_high_path, 'w')
temperature_file_low = open ( temperature_file_low_path, 'w')

with open(noteevent_file_path) as in_file:
    for line in in_file:
        line = re.sub(r'[-|,]', ' ', line)
        matchObj = re.match(r'.* temp\D*\s\D{0,5}(\d+(?:\.\d*)?|\.\d+)\s+(\S+)', line, re.I)
        if not matchObj:
           matchObj = re.match(r'^temp\D*\s\D{0,5}(\d+(?:\.\d*)?|\.\d+)\s+(\S+)', line, re.I)
        
        if matchObj:
            temperature_string = matchObj.group(1)
            temperature = float(matchObj.group(1))
            print ("line: " , matchObj, "temp ", temperature)
            if temperature < 50:
                #print ('convert celsius ', temperature)
                fahreheit_temperature = ( temperature * 9 ) / 5 + 32
                line = line.replace(temperature_string, str ( fahreheit_temperature) )
            else:
                fahreheit_temperature = temperature
            
            if fahreheit_temperature > 99:
                temperature_file_high.write(line)
            else:
                temperature_file_low.write(line)
                
temperature_file_high.close()
temperature_file_low.close()
