#!/usr/bin/python

import gzip
import io
################################################################################# SRR3879604
# set dictionary and counters to empty or 0
bc_dic604 = {}
total_bc_count604 = 0
dic_count604 = 0
total_repeat_count604 = 0
no_bc_count604 = 0
# open with gzip, make sure to use 'rt'
with io.TextIOWrapper(io.BufferedReader(gzip.open('/projectnb/bf528/project_4_scrnaseq/fastq/SRR3879604/SRR3879604_1_bc.fastq.gz'))) as sample604:
    # loop through each line, gather barcodes, count barcode frequency, store count for non-bc samples too
    for line in sample604:
        if line[0] == '@':
            next_line = next(sample604)
            barcode = next_line[0:19]
            if barcode in bc_dic604:
                total_bc_count604 += 1
                total_repeat_count604 += 1
                bc_dic604[barcode] += 1
            if barcode not in bc_dic604:
                total_bc_count604 += 1
                dic_count604 += 1
                bc_dic604[barcode] = 1
            else:
                no_bc_count604 += 1
    no_bc = "no bc"
    bc_dic604[no_bc] = no_bc_count604
# write dic to file
sample604.close()
#f604 = open("bc_unique604_v2.txt", "w")
#f604.write(str(bc_dic604))
#f604.close()

f = open("bc_meta_v2.2.s4.txt", "w")
f.write("\t\t total barcodes \t dictionary count \t repeats \n")
f.write("SRR3879604: \t "+str(total_bc_count604)+"\t\t\t\t"+str(dic_count604)+"\t\t\t\t"+str(total_repeat_count604)+"\n")
f.close()
