#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:30:22 2022

@author: asep
"""

import pandas as pd
filename = ['raw/lsverbalization121k.csv']
en_dataset = pd.read_csv(filename, delimiter='\t')
print(en_dataset.head())