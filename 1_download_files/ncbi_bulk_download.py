"""
Created on Sat Sept 4 11:41:25 2021

@author: agustinwagner

Este script se ejecuta desde la consola, requiere dos flags, ejemplo:

python ncbi_bulk_download.py -i file.csv -t genomic.fna.gz

Funciona con los .csv que se pueden descargar desde la página de NCBI.
"""

#Importo las librerías
import urllib3
import pandas as pd
import argparse
import gzip
import shutil
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file (csv)")
#genomic.fna.gz
#protein.faa.gz
parser.add_argument("-t", "--type", help="Type of file, with extension")

args = parser.parse_args()

http = urllib3.PoolManager()
urllib3.disable_warnings()

# Leo el archivo csv (flag -i) generado en 
# https://www.ncbi.nlm.nih.gov/genome/browse#!/prokaryotes/508/
data = pd.read_csv(args.input)

#Guardo las direcciones FTP en una variable
genBank_links = data["GenBank FTP"]

#Por cada dirección FTP (una por cada sample), descargo el archivo requerido (flag -t)
for link in genBank_links:
    http_link = link.replace("ftp", "https", 1)
    
    splited_link = link.split("/")
    id = splited_link[len(splited_link)-1]
    fileName = id + "_" + args.type
    type_of_data = args.type.split(".")[0]
    unzipped_extension = args.type.split(".")[1]
    unzipped_name = id+"_"+type_of_data+"."+unzipped_extension

    print("Downloading from " + http_link + "/" + id + "_"  + args.type)
    with urllib3.PoolManager() as http:
        r = http.request('GET', http_link + "/" + id + "_"  + args.type)
        with open(fileName, 'wb') as fout:
            fout.write(r.data)

    with gzip.open(fileName, 'rb') as f_in:
        print("Unzipping as " + unzipped_name)
        with open(unzipped_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            
    source = unzipped_name
    destination = type_of_data
    new_path = shutil.move(source, destination)
    if os.path.exists(fileName):
        os.remove(fileName)
        print("Deleted .gz file")
print("Finished")