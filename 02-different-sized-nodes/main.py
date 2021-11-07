import networkx as nx
from networkx.algorithms.centrality import degree_centrality, betweenness_centrality, eigenvector_centrality, harmonic_centrality, closeness_centrality
import pandas as pd
import matplotlib.pyplot as plt

#*******************************************************************************************
#   PRINTANDO O GRAFO CLASSIFICANDO O TAMANHO DO NÓ DE ACORDO COM A IMPORTÂNCIA 
#                                  APENAS 35 LINHAS
#******************************************************************************************
fungal_file = pd.read_csv('Foxysporum_network.csv')
tf_nodes = fungal_file["tf_locus_tag"].to_list()[0:35]
tg_nodes = fungal_file["tg_locus_tag"].to_list()[0:35]

edges = list(zip(tf_nodes, tg_nodes))
DG = nx.DiGraph()
DG.add_edges_from(edges)
nx.set_node_attributes(DG, betweenness_centrality(DG), name="size")
subax1 = plt.subplot(121)

layout = nx.spring_layout(DG)
nx.draw_networkx_edges(DG, layout)
node_list = nx.get_node_attributes(DG, 'size')
nx.draw_networkx_nodes(DG, layout, nodelist=node_list.keys(), node_size=[n * 1000 for n in node_list.values()])
plt.show()

#************************************************
