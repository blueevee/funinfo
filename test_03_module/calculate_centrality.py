import networkx as nx
from networkx.algorithms.centrality import degree_centrality,closeness_centrality, betweenness_centrality, eigenvector_centrality, harmonic_centrality
import pandas as pd


### Cria o grafo baseado na lib neworkX usando as
### infos recebidas com os genes ltf e tg do fungo
def create_graph(fungal_file: str):
    fungal_data = pd.read_csv(fungal_file)
    tf_nodes = fungal_data["tf_locus_tag"].tolist()
    tg_nodes = fungal_data["tg_locus_tag"].tolist()
    edges = list(zip(tf_nodes, tg_nodes))
    DG = nx.DiGraph()
    DG.add_edges_from(edges)
    return DG

### A partir do grafo calcula a degree centrality
def calculate_degree_centrality(fungal_file: str):
    graph = create_graph(fungal_file)
    return degree_centrality(graph)

### A partir do grafo calcula a closeness centrality
def calculate_closeness_centrality(fungal_file: str):
    graph = create_graph(fungal_file)
    return closeness_centrality(graph)

### A partir do grafo calcula a betweenness centrality
def calculate_betweenness_centrality(fungal_file: str):
    graph = create_graph(fungal_file)
    return betweenness_centrality(graph)

### A partir do grafo calcula a eigenvector centrality
def calculate_eigenvector_centrality(fungal_file: str):
    graph = create_graph(fungal_file)
    return eigenvector_centrality(graph)

### A partir do grafo calcula a harmonic centrality
def calculate_harmonic_centrality(fungal_file: str):
    graph = create_graph(fungal_file)
    return harmonic_centrality(graph)
