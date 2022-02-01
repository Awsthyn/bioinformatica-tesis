import seaborn as sns
import pandas as pd
sns.set_theme(color_codes=True)
df = pd.read_csv("all_vs_all_ani_summary.csv", index_col="Genome A")
df = df.drop('Unnamed: 0', axis=1)
df.round(0) 
g = sns.clustermap(df, annot=True, annot_kws={"size": 7}, fmt='.3g', cbar_pos=(0, .2, .03, .4),figsize=(18,12))
fig = g.fig
fig.savefig("ANI_Tree") 

