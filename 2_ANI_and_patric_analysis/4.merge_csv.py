#Importo las librerías
import pandas as pd

ids_file = pd.read_csv("IdsFile.csv")
max_ani_summary = pd.read_csv("max_ani_summary.csv")
patric_quality_summary = pd.read_csv("patric_quality_summary.csv")
merged_df = ids_file.merge(max_ani_summary, left_on="genome_file", right_on='Genome A', how='outer')
merged_third_csv = merged_df.merge(patric_quality_summary, left_on="scientific name", right_on='Genome Name', how='outer')
merged_third_csv.to_csv('final_summary.tsv', sep="\t", encoding='utf-8', index=False)
