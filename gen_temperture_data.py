#!/usr/bin/python

import re

noteevent_file_path = "C:/Users/Brian/workspace/nlp/NOTEEVENTS.csv"
temperture_file_high_path = "c:/Users/Brian/workspace/nlp/NOTEEVENTS_high_temperture.txt"
temperture_file_low_path = "c:/Users/Brian/workspace/nlp/NOTEEVENTS_low_temperture.txt"

temperture_file_high = open ( temperture_file_high_path, 'w')
temperture_file_low = open ( temperture_file_low_path, 'w')

with open(noteevent_file_path) as in_file:
    for line in in_file:
        line = re.sub(r'[-|,]', ' ', line)
        matchObj = re.match(r'.* temp\D*\s\D{0,5}(\d+(?:\.\d*)?|\.\d+)\s+(\S+)', line, re.I)
        if not matchObj:
           matchObj = re.match(r'^temp\D*\s\D{0,5}(\d+(?:\.\d*)?|\.\d+)\s+(\S+)', line, re.I)
        
        if matchObj:
            temperture_string = matchObj.group(1)
            temperture = float(matchObj.group(1))
            print ("line: " , matchObj, "temp ", temperture)
            if temperture < 50:
                #print ('convert celsius ', temperture)
                fahreheit_temperture = ( temperture * 9 ) / 5 + 32
                line = line.replace(temperture_string, str ( fahreheit_temperture) )
            else:
                fahreheit_temperture = temperture
            
            if fahreheit_temperture > 99:
                temperture_file_high.write(line)
            else:
                temperture_file_low.write(line)
                
temperture_file_high.close()
temperture_file_low.close()
