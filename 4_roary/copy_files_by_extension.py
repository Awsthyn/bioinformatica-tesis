import shutil
import os

#Este archivo recorre todas las subcarpetas contenidas en la carpeta (path), y copia los archivos de la extensión requerida.


path = "./prokka_output"
list_of_folders = os.listdir(path)
#.gff para roary, .faa para GET_HOMOLOGUES
file_extension = ".faa"

for folder in list_of_folders:
    content = os.listdir(path+"/"+folder)
    for file in content:
        if(file[-4:len(file)] == file_extension):
            shutil.copy(path+"/"+folder+"/"+file,
            #./gff para roary, ./faa para GET_HOMOLOGUES
             './faa/'+folder+file_extension)