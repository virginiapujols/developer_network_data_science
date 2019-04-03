import networkx as nx
import GitManager

# Create an empty graph with no nodes and no edges.
G = nx.Graph()


# Add a list of nodes
def create_nodes(node_list, edges_list):
    G.add_nodes_from(node_list)



