# Readme 

## Files 

We have the following files:
* data.csv - insert data here
* dataset.csv - automatically generated file with tokenization etc. Don't touch it;
* learners.csv - a table where are stored the infos of the learners

## data.csv
The table of the entries
## dataset.csv
The automatically generated table of the entries by the script /lib/generator.py


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

### item-id 
univoque identifier for the entry

### learner-id
univoque id for the learner, linked to learners.csv

### content
the entry

## learners.csv 
Table of learners, including grades, languages, ID, ecc.

### languages 

Languages are written with the standard ISO 639-1 code [wiki](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
