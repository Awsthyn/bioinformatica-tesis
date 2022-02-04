import pandas as pd
import os
#['pair#', 'orthoANI_value', 'avg_aligned_length', 'query_coverage', 'subject_coverage', 'query_length', 'subject_length\n']

folder_path = "./output"

list_of_ANI_reports = os.listdir(folder_path)


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

list_of_ANI_reports = list_files(folder_path)

d = {"Genome A": [],
    "Genome B": [],
    "orthoANI_value": []
}

def get_names(lines):
        split_by_tabulation = lines[2].split("\t")
        split_by_slash = split_by_tabulation[1].split("/")
        genome_A_split_by_dot = split_by_slash[6].split(".fna")
        genome_B_split_by_dot = split_by_slash[12].split(".fna")
        d["Genome A"].append(genome_A_split_by_dot[0])
        d["Genome B"].append(genome_B_split_by_dot[0])



for file in list_of_ANI_reports:
        lines = []
        with open(file) as f:
                lines = f.readlines()
        values = lines[8].split("\t")
        get_names(lines)
        d["orthoANI_value"].append(float(values[1]))

df = pd.DataFrame(data=d)
comparison=df['Genome B'].unique()
df2=pd.concat([df.set_index(['Genome A']).groupby('Genome B')['orthoANI_value'].get_group(key) for key in comparison],axis=1)
df2.columns=comparison
df2.reset_index(inplace=True)
df2.to_csv('all_vs_all_ani_summary.tsv', sep="\t", encoding='utf-8')
