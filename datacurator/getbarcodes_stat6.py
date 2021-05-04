#!/usr/bin/python

import gzip
import io
################################################################################# SRR3879606
# set dictionary and counters to empty or 0
bc_dic606 = {}
total_bc_count606 = 0
dic_count606 = 0
total_repeat_count606 = 0
no_bc_count606 = 0
# open with gzip, make sure to use 'rt'
with io.TextIOWrapper(io.BufferedReader(gzip.open('/projectnb/bf528/project_4_scrnaseq/fastq/SRR3879606/SRR3879606_1_bc.fastq.gz'))) as sample606:
   # loop through each line, gather barcodes, count barcode frequency, store count for non-bc samples too
    for line in sample606:
        if line[0] == '@':
            next_line = next(sample606)
            barcode = next_line[0:19]
            if barcode in bc_dic606:
                total_bc_count606 += 1
                total_repeat_count606 += 1
                bc_dic606[barcode] += 1
            if barcode not in bc_dic606:
                total_bc_count606 += 1
                dic_count606 += 1
                bc_dic606[barcode] = 1
            else:
                no_bc_count606 += 1
    no_bc = "no bc"
    bc_dic606[no_bc] = no_bc_count606
# write dic to file
sample606.close()
#f606 = open("bc_unique606_v2.txt", "w")
#f606.write(str(bc_dic606))
#f606.close()

f = open("bc_meta_v2.2.s6.txt", "w")
f.write("\t\t total barcodes \t dictionary count \t repeats \n")
f.write("SRR3879606: \t "+str(total_bc_count606)+"\t\t\t\t"+str(dic_count606)+"\t\t\t\t"+str(total_repeat_count606)+"\n")
f.close()
