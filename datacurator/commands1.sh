module load salmon

# get transcript and primary_assembly files
wget \
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_37/gencode.v37.transcripts.fa.gz
wget \
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_37/GRCh38.primary_assembly.genome.fa.gz

# generate decoys text for salmon index
grep "^>" <(gunzip -c GRCh38.primary_assembly.genome.fa.gz) | cut -d " " -f 1 > decoys.txt
sed -i.bak -e 's/>//g' decoys.txt

# generate transcript text for salmon index
cat gencode.v37.transcripts.fa.gz GRCh38.primary_assembly.genome.fa.gz > gentrome.fa.gz
