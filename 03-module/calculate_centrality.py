import networkx as nx
from networkx.algorithms.centrality import degree_centrality,closeness_centrality, betweenness_centrality, eigenvector_centrality, harmonic_centrality
import pandas as pd


def create_graph(fungal):
    tf_nodes = fungal["tf_locus_tag"].to_list()
    tg_nodes = fungal["tg_locus_tag"].to_list()
    edges = list(zip(tf_nodes, tg_nodes))
    DG = nx.DiGraph()
    DG.add_edges_from(edges)
    return DG

def calculate_degree_centrality(fungal):
    fungal_data = pd.DataFrame(fungal)
    graph = create_graph(fungal_data)
    return degree_centrality(graph)

def calculate_closeness_centrality(fungal):
    fungal_data = pd.DataFrame(fungal)
    graph = create_graph(fungal_data)
    return closeness_centrality(graph)

def calculate_betweenness_centrality(fungal):
    fungal_data = pd.DataFrame(fungal)
    graph = create_graph(fungal_data)
    return betweenness_centrality(graph)

def calculate_eigenvector_centrality(fungal):
    fungal_data = pd.DataFrame(fungal)
    graph = create_graph(fungal_data)
    return eigenvector_centrality(graph)

def calculate_harmonic_centrality(fungal):
    fungal_data = pd.DataFrame(fungal)
    graph = create_graph(fungal_data)
    return harmonic_centrality(graph)
