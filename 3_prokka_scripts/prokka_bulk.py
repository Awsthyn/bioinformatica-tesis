"""
Created on Fri Aug 20 21:41:49 2021

@author: agustinwagner

cd /media/agustinwagner/44743DB9743DAE94/Tesis/archivos\ fasta/
"""

import subprocess
import os

path_fna_container = "./genomic"
list_of_samples = os.listdir(path_fna_container)

for sample in list_of_samples:
    split_name = sample.split(".")
    bash_command = 	"prokka --kingdom Bacteria --outdir ./prokka_output/prokka_"
    + split_name[0] +" --genus Rhodopseudomonas --locustag "
    + split_name[0] 
    +" "+path_fna_container + sample
    
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

