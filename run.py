#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:17:29 2022

@author: asep
"""

import pandas as pd
filenames = ['train.txt', 'dev.txt', 'test.txt']
dfs=[]
for filename in filenames:
    df = pd.read_csv("dataset/DE/test.txt", delimiter="\t")
    dfs.append(df)

df = pd.concat(dfs, axis=0, ignore_index=True)
max_value_ls = df["ls"].max()
max_value_verbalization = df["verbalization"].max()    

print("")
print("##### Dataset samples #####")
print(df.sample(10))
print(f"max length for ls: {max_value_ls}")
print(f"max length for verbalization: {max_value_verbalization}")