import pandas as pd
import os

path = "./csv_files"
list_of_samples = os.listdir(path)
df_array = []
for file in list_of_samples:
    df_array.append(pd.read_csv(path+"/"+file))

strain_dictionary = {
    "genome_file": [],
    "scientific name": []

}
for df in df_array:
    for index, row in df.iterrows():
        specie_array = row['#Organism Name'].split(" ")
        strain_dictionary["genome_file"].append(row["Assembly"].split(".")[0])
        
        strain_dictionary["scientific name"].append(specie_array[0] + " " 
        + specie_array[1] + ("" if pd.isna(row['Strain']) else " " + str(row['Strain'])))
new_df = pd.DataFrame(strain_dictionary)
new_df.to_csv('IdsFile.csv', encoding='utf-8', index=False)
