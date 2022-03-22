#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:30:22 2022

@author: asep
"""

import pandas as pd
filename = 'dataset/raw/lsverbalization121k.csv'
df_en = pd.read_csv(filename, delimiter=',')
print(df_en.head())
print(df_en.describe(include='all'))
ls_len_max = df_en["ls"].str.len().max()
verbalization_len_max = df_en["verbalization"].str.len().max()
print(ls_len_max, verbalization_len_max)

from sklearn.utils import shuffle
df = shuffle(df_en)
df.to_csv(f"df.csv", sep ='\t')
df_dataset = {}
start = 1
end = 101
for i in range(20):
    df_dataset[i+1] = df[start:end]
    df_dataset[i+1].to_csv(f"df_{i+1}.csv", sep ='\t')
    start +=100
    end +=100

dfs=[]    
for i in range(20):
    df = pd.read_csv(f"df_{i+1}.csv", delimiter='\t')
    dfs.append(df)

all_dfs = pd.concat(dfs, axis=0, ignore_index=True)
print(all_dfs.describe(include='all'))