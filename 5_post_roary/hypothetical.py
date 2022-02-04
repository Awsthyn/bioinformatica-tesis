import pandas as pd
from Bio import SeqIO

df = pd.read_csv("gene_presence_absence.csv",low_memory=False)

hypotheticals = df[(df["Annotation"] == "hypothetical protein")]

# Data structure to use an O(n) algorithm (and avoid a O(n^2) algorithm).
hash_table = {}

for index, row in hypotheticals.iterrows():
    hash_table[row['Gene']] = True


for seq_record in SeqIO.parse("pan_genome_reference.fa", "fasta"):
     gene = seq_record.description.split()[1]
     if(gene in hash_table):
          hash_table[gene] = str(seq_record.seq)

with open('hypothetical_genes.csv', 'w') as f:
    for key in hash_table.keys():
        f.write("%s,%s\n"%(key,hash_table[key]))