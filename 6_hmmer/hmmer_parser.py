import pandas as pd
import re
import csv

file1 = open('./AzulInAllTable.txt', 'r')
Lines = file1.readlines()
arrays =  [["E-value", "score", "bias", "Sequence","start","end","Description"]]

# Strips the newline character
for line in Lines:
     tempArray = re.split(r'\s+',line)
     description = " ".join(tempArray[7::])
     arrays.append(tempArray[1:7] + [description])



with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(arrays)
