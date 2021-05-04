#!/usr/bin/python

import gzip
import io
################################################################################# SRR3879605
# set dictionary and counters to empty or 0
bc_dic605 = {}
total_bc_count605 = 0
dic_count605 = 0
total_repeat_count605 = 0
no_bc_count605 = 0
# open with gzip, make sure to use 'rt'
with io.TextIOWrapper(io.BufferedReader(gzip.open('/projectnb/bf528/project_4_scrnaseq/fastq/SRR3879605/SRR3879605_1_bc.fastq.gz'))) as sample605:
    # loop through each line, gather barcodes, count barcode frequency, store count for non-bc samples too
    for line in sample605:
        if line[0] == '@':
            next_line = next(sample605)
            barcode = next_line[0:19]
            if barcode in bc_dic605:
                total_bc_count605 += 1
                total_repeat_count605 += 1
                bc_dic605[barcode] += 1
            if barcode not in bc_dic605:
                total_bc_count605 += 1
                dic_count605 += 1
                bc_dic605[barcode] = 1
            else:
                no_bc_count605 += 1
    no_bc = "no bc"
    bc_dic605[no_bc] = no_bc_count605
# write dic to file
sample605.close()
#f605 = open("bc_unique605_v2.txt", "w")
#f605.write(str(bc_dic605))
#f605.close()

f = open("bc_meta_v2.2.s5.txt", "w")
f.write("\t\t total barcodes \t dictionary count \t repeats \n")
f.write("SRR3879605: \t "+str(total_bc_count605)+"\t\t\t\t"+str(dic_count605)+"\t\t\t\t"+str(total_repeat_count605)+"\n")
f.close()
