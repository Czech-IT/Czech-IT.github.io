#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk import *
import string
item = """Dottor Bolpagni senta: secondo me la cosa che che mi hanno fatto, cioè la scrittura Forza
Juve nel vestito, secondo me è un è una bella cosa che ci farà divertire tutti. Quindi a me
veramente non mi dà senso che tu non l’abbia gradito """
tokens = nltk.word_tokenize(item)
print(tokens)
punctuations = list(string.punctuation)
leng=len([i.strip("".join(punctuations)) for i in word_tokenize(item) if i not in punctuations])
print(leng)