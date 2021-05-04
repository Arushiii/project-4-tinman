#!/usr/bin/python

import pandas as pd
import numpy as np

orig_file = pd.read_csv("/projectnb/bf528/users/tinman/Project4/datacurator/txp2gene_pre.tsv", sep='|')

file = pd.DataFrame(orig_file).to_numpy()

txp2gene = open("txp2gene_v2.txt", "w")

for line in file:
    txp2gene.write("ENST00000456328.2\tENSG00000223972.5\n"+str(line[0])+'\t'+str(line[1])+'\n')

txp2gene.close()
