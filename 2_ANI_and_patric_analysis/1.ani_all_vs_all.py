import os
import subprocess

#path donde están los archivos fasta,
path = "./fasta_nombres_dicientes"

list_of_genomes = os.listdir(path)

#Dos ciclos for (time complexity = O(n^2))
#Se puede reducir el tiempo a la mitad, porque cada especie se compara con otra 2 veces (A se compara con B, y después B con A). Faltaría agregar un condicional para que esto no ocurra.
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
            #el siguiente comando bash, ejecutado con JAVA, tiene los siguientes argumentos:
            #-jar path de OAU.jar , el script que realiza el ANI 1 vs 1.
            #-f1 y -f2 path del archivo fasta 1, y path del archivo fasta 2.
            #-o path donde se va a guardar el resultado.
            #-n núcleos del procesador que se van a destinar a esta tarea.
            bash_command = f"java -jar OAU.jar -u /home/agustinwagner/Documents/Tesis/ANI/usearch  -f1 /home/agustinwagner/Documents/Tesis/fasta_nombres_dicientes/{file} -f2 /home/agustinwagner/Documents/Tesis/fasta_nombres_dicientes/{comparison} -o /home/agustinwagner/Documents/Tesis/output/{primary_genome}/{secondary_genome} -n 4"
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
