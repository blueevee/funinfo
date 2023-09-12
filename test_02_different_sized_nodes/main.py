import networkx as nx
from networkx.algorithms.centrality import degree_centrality, betweenness_centrality, eigenvector_centrality, harmonic_centrality, closeness_centrality
import matplotlib.pyplot as plt
import pandas as pd


fungal_file = pd.read_csv('Foxysporum_network.csv')
tf_nodes = fungal_file["tf_locus_tag"].to_list()
tg_nodes = fungal_file["tg_locus_tag"].to_list()

edges = list(zip(tf_nodes, tg_nodes))
DG = nx.DiGraph()
DG.add_edges_from(edges)

centrality = sorted(closeness_centrality(DG).items(), reverse =True, key=lambda x: x[1])
# centrality = sorted(betweenness_centrality(DG).items(), reverse =True, key=lambda x: x[1])
# print(centrality)

# Dicionário com tag e importância do nó de acordo com a centralidade
# ordered_dict = {tag: value for tag, value in centrality}

node_sizes = [centrality[node] * 2000 for node in DG.nodes()]
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(DG)
nx.draw_networkx_edges(DG, pos)
nx.draw_networkx_nodes(DG, pos, node_color='#AED6F1', node_size=node_sizes)
nx.draw_networkx_labels(DG, pos, font_color='#0a1e2c', font_size=8)
plt.axis('off')
plt.show()
