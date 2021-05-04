#!/usr/bin/python

import ast
import numpy as np
import matplotlib.pyplot as plt
import pprint
import pandas
##############################################################################################################
sample604 = open("/projectnb/bf528/users/tinman/Project4/datacurator/bc_unique604_v2.txt",'r')
s4 = sample604.read()
s4dic = ast.literal_eval(s4)

sample605 = open("/projectnb/bf528/users/tinman/Project4/datacurator/bc_unique605_v2.txt",'r')
s5 = sample605.read()
s5dic = ast.literal_eval(s5)

sample606 = open("/projectnb/bf528/users/tinman/Project4/datacurator/bc_unique606_v2.txt",'r')
s6 = sample606.read()
s6dic = ast.literal_eval(s6)
##############################################################################################################
big_dic = {}

dic_list = s4dic, s5dic, s6dic
for sample in dic_list:
    for barcode, count in sample.items():
        if barcode not in big_dic:
            big_dic[barcode] = count
        elif barcode in big_dic:
            big_dic[barcode] += count
##############################################################################################################
count = 0
if count < 100:
    for ithem,v in big_dic.items():
        print(ithem,v)
        count +=1
##############################################################################################################
unique_all = open("all_unique_bc_count.csv", "w")

for key,value in big_dic.items():
    if key != "no bc":
        unique_all.write(str(key) + ',' + str(value) + '\n')
unique_all.close()
