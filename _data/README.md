# Readme 

## Files 

We have 3 files:
* dataset.csv - which contains raw data;
* learners.csv - a table where are stored the infos of the learners
* annotations-dataset.csv - in which every item in dataset.csv's rows are marked, either manually than automatically

## dataset.csv
The table of the entries
### item-id 
univoque identifier for the entry

### learner-id
univoque id for the learner, linked to learners.csv

### content
the entry

## learners.csv 
Table of learners, including grades, languages, ID, ecc.

## annotations-dataset.csv
The table for the annotations
### item-id
linked to dataset.csv

### manual-phenomena
array of categories

### auto-tokenize
obtained with Python nltk:
```
  >>> item = """ ((content)) """
  >>> nltk.word_tokenize(item)
```
### auto-count-words
obtained with Python nltk:
```
  >>> import string
  >>> punctuations = list(string.punctuation)
  >>> len([i.strip("".join(punctuations)) for i in word_tokenize(item) if i not in punctuations])
```
### auto-pos
In progress with TreeTagger

### notes
manual notes on the entries
