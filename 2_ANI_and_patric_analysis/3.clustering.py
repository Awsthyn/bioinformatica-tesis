import seaborn as sns
import pandas as pd

#En el .csv usado como input, reemplazar ",," por ",100.00," y la primera línea, al final, después de la coma, agregar "100.00". Si no, da error.
#Lo anterior ocurre porque no se hizo el ANI contra sí mismo (no tiene sentido, es 100%), y al no tener ese dato, es un NaN, y el cluster acepta solamente números.

sns.set_theme(color_codes=True)

#Esta función se usa para poner en cursiva el género y la especie, y poner la T del final como superíndice.
def customize_name(name):
    name_list = name.split(" ")
    gender= r'$\it{' + name_list[0].replace(' ', '\\ ') + '}$'
    specie = r'$\it{' + name_list[1].replace(' ', '\\ ') + '}$'
    if(name == "Rhodopseudomonas rutila TIE-1"):
        return(gender + ' ' + specie + ' ' + name_list[2])
    elif(len(name_list) == 3):
        return(gender + ' ' + specie + ' ' + name_list[2].replace("T",r'$\ ^T$'))
    else: 
        return(gender + ' ' + specie + ' ' + name_list[2] + ' ' + name_list[3].replace("T",r'$\ ^T$'))


df = pd.read_csv("all_vs_all_ani_summary.csv", index_col="Genome A")
df = df.drop('Unnamed: 0', axis=1)
df.round(0) 

#El núcleo de este archivo, sns.clustermap genera el heatmap + clustering.
g = sns.clustermap(df, annot=True, annot_kws={"size": 7}, fmt='.3g', cbar_pos=(0, .2, .03, .4),figsize=(18,12))

#Acá seteamos los estilos, con la función customize_name definida más arriba.
g.ax_heatmap.set_yticklabels([customize_name(ticklabel.get_text())
                              for ticklabel in g.ax_heatmap.get_yticklabels()])
g.ax_heatmap.set_xticklabels([customize_name(ticklabel.get_text())
                              for ticklabel in g.ax_heatmap.get_xticklabels()])

#Guardamos la imagen generada.
fig = g.fig
fig.savefig("ANI_Tree.png", format="png") 

