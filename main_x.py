# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:06:01 2021

@author: karthik
"""

import pandas as pd
import numpy as np

import os


os.getcwd() 

test_set = pd.read_csv("data/test.csv")
train_set = pd.read_csv("data/train.csv")
print("Data Set Columns: {}".format(train_set.columns))
print(train_set.head())
