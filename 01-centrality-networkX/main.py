import networkx as nx
from networkx.algorithms.centrality import degree_centrality, betweenness_centrality, eigenvector_centrality, harmonic_centrality, closeness_centrality
import pandas as pd


#* Transformei o arquivo num csv
tsv_file='Foxysporum_network.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('Foxysporum_network.csv',index=False)

#* Os nós são tf_locus_tag e tg_locus_tag e as arestas são as linhas que representam ligações entre os nós tf e tg
fungal_file = pd.read_csv('Foxysporum_network.csv')
tf_nodes = fungal_file["tf_locus_tag"].to_list()
tg_nodes = fungal_file["tg_locus_tag"].to_list()

edges = list(zip(tf_nodes, tg_nodes))
DG = nx.DiGraph()
DG.add_edges_from(edges)
top_5_degree = sorted(degree_centrality(DG).items(),reverse =True, key=lambda x: x[1])
top_5_btw = sorted(betweenness_centrality(DG).items(), reverse =True, key=lambda x: x[1])
top_5_clo = sorted(closeness_centrality(DG).items(),reverse =True, key=lambda x: x[1])
top_5_eig = sorted(eigenvector_centrality(DG).items(),reverse =True, key=lambda x: x[1])
top_5_harm = sorted(harmonic_centrality(DG).items(),reverse =True, key=lambda x: x[1])

print(f"DEGREE::::{top_5_degree[0:5]}")
print(f"\nBETWEENNESS:::{top_5_btw[0:5]}")
print(f"\nEIGENVECTOR:::{top_5_eig[0:5]}")
print(f"\nHARMONIC:::{top_5_harm[0:5]}")
print(f"\nCLOSENESS:::{top_5_clo[0:5]}")