#!/usr/bin/env python
# -*- coding: utf-8 -*-


###############################################################
# Import libraries
###############################################################

import csv, nltk, string


###############################################################
# Variables
###############################################################

outfile         = open('../_data/dataset.csv', 'w',  encoding="utf-8", newline='')

write_outfile   = csv.writer(outfile)

punctuations    = list(string.punctuation)

header          = ['item-id', 'learner-id', 'type' ,'content', 'date', 'manual-phenomena', 'notes',  'auto-tokenize', 'auto-count-words']

###############################################################
# Functions
###############################################################

# TODO/TOFIX

# def preprocess(item):
#     item = row.lower()
#     toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
#     tokens = toker.tokenize(item)# 

# def process(row):
#     row = str(row)
#     token = print(nltk.word_tokenize(row))
#     tokenLen = len([i for i in nltk.word_tokenize(row) if i not in punctuations])





###############################################################
# Operations
###############################################################

# Write the header
#write_outfile.writerow(header)

# Open the file
with open('../_data/data.csv', 'r', encoding='utf8', newline='') as csvfile:  # this will close the file automatically.
    reader      = csv.reader(csvfile)

    write_outfile.writerow(header)

# Loop

    for row in reader:

# Set variables inside the loop ## I DON'T THINK IT IS SO GOOD BUT NOW IT WORKS

        item    = str(row[3])
        token   = nltk.word_tokenize(item)
        # token = i for i in nltk.word_tokenize(item) if i not in punctuations
        tokenLen    = len([i for i in nltk.word_tokenize(item) if i not in punctuations])

        masterList  = []
        masterList.append(row[0])    
        masterList.append(row[1])    
        masterList.append(row[2])    
        masterList.append(row[3])    
        masterList.append(row[4])    
        masterList.append(row[5])       
        masterList.append(row[6])       
        masterList.append(token)
        masterList.append(tokenLen)

# Output

        
        write_outfile.writerow(masterList)        
        


###############################################################

