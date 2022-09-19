import pandas as pd
from Bio import SeqIO


import xlrd
book = xlrd.open_workbook('Rhodopseudomonas.5.8.22.xls')
sheet = book.sheet_by_name('shared')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# Profit !
list_of_genes = []
for x in data:
  list_of_genes.append(x[0])
del list_of_genes[0]

df = pd.read_csv("gene_presence_absence.csv",low_memory=False)

hypotheticals = df[df["Annotation"].isin(list_of_genes)]
# Data structure to use an O(n) algorithm (and avoid a O(n^2) algorithm).
'''
hash_table = {}

for index, row in df.iterrows():
    hash_table[row['Gene']] = True


for seq_record in SeqIO.parse("pan_genome_reference.fa", "fasta"):
     gene = seq_record.description.split()[1]
     if(gene in hash_table):
          hash_table[gene] = str(seq_record.seq)

with open('total_genes.csv', 'w') as f:
    for key in hash_table.keys():
        f.write("%s,%s\n"%(key,hash_table[key]))
'''
# Data structure to use an O(n) algorithm (and avoid a O(n^2) algorithm).
hash_table = {}

for name in list_of_genes:
    hash_table[name] = True
for seq_record in SeqIO.parse("pan_genome_reference.fa", "fasta"):
     gene = seq_record.description.split()[1]
     if(gene in hash_table):
          hash_table[gene] = str(seq_record.seq)

with open('shared_genes.csv', 'w') as f:
    for key in hash_table.keys():
        f.write("%s,%s\n"%(key,hash_table[key]))
