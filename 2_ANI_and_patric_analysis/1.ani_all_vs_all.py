import pandas as pd
import os
import subprocess

path = "./fasta_nombres_dicientes"
list_of_genomes = os.listdir(path)
for file in list_of_genomes:
    primary_genome = file[0:-4]
    if(os.path.isdir(f"output/{primary_genome}") == False):
        bash_to_create_folder = f"mkdir output/{primary_genome}"
        process = subprocess.Popen(bash_to_create_folder.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()   
    for comparison in list_of_genomes:
        secondary_genome = comparison[0:-4]
        if(file != comparison and os.path.isfile(f"output/{primary_genome}/{secondary_genome}") == False):
            print(f"{primary_genome} vs {secondary_genome}")
            bash_command = f"java -jar OAU.jar -u /home/agustinwagner/Documents/Tesis/ANI/usearch  -f1 /home/agustinwagner/Documents/Tesis/fasta_nombres_dicientes/{file} -f2 /home/agustinwagner/Documents/Tesis/fasta_nombres_dicientes/{comparison} -o /home/agustinwagner/Documents/Tesis/output/{primary_genome}/{secondary_genome} -n 4"
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
