# get salmon index
salmon-latest_linux_x86_64/bin/salmon index -t gentrome.fa.gz -d decoys.txt -p 12 -i index --gencode

# get salmon map part 1/2
grep "^>" <(gunzip -c gencode.v37.transcripts.fa.gz) | cut -d " " -f 1,7 --output-delimiter=$'\t' - | sed 's/[>"gene_symbol:"]//g' > txp2gene_pre.tsv

# run my python get_map to get salmon part 2/2 then...
cp /usr4/bf527/tpillars/Documents/tinman_project4/txp2gene.txt .

#rename txp2gene.txt > txp2gene.tsv
