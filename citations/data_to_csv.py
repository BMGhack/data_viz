# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:15:37 2020

@author: Tim
"""

from xlsx2csv import Xlsx2csv
from os import listdir
from os.path import isfile, join

datafiles = [f for f in listdir('data') if isfile(join('data', f)) and f.endswith('.xlsx')]
for i in range(7,len(datafiles)):
    Xlsx2csv("data/" + datafiles[i], outputencoding="utf-8").convert("data/" + datafiles[i].split('.')[0] + ".csv")