import networkx as nx
import pandas as pd

def build_payment_graph(edges: pd.DataFrame) -> nx.DiGraph:
    graph = nx.DiGraph()
    for _, row in edges.iterrows():
        graph.add_edge(row["source"], row["target"], relationship=row.get("relationship", "pays"))
    return graph

def compute_payment_graph_features(graph: nx.DiGraph) -> dict:
    return {
        "node_count": graph.number_of_nodes(),
        "edge_count": graph.number_of_edges(),
        "degree_centrality": nx.degree_centrality(graph),
        "pagerank": nx.pagerank(graph) if graph.number_of_nodes() > 0 else {}
    }
