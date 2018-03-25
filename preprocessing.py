# -*- coding: utf-8 -*-
import numpy as np

#load data
file=open("weibo_train_data.txt",encoding="utf-8")

lines=file.readlines()
rows=len(lines)

datamat=np.zeros((rows,3))

row=0
for line in lines:
    line=line.strip().split('\t')
    datamat[row, 0] = line[3]
    datamat[row, 1] = line[4]
    datamat[row, 2] = line[5]
    row+=1

print(datamat)
print(datamat.shape)