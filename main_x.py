# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:06:01 2021

@author: karthik
"""

import pandas as pd
import os


os.getcwd() 

test_set = pd.read_csv("datasets/text.csv")
train_set = pd.read_csv("datasets/train.csv")
