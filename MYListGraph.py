

class Node:
    def __init__(self, index, data):
        self.index = index
        self.data = data


class Edge:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b


class EdgeList:
    def __init__(self, node):
        self.node = node  # Node object
        self.edges = []  # list of Edge objects

    def add_edge(self, edge):
        self.edges.append(edge)


class ListGraph:
    def __init__(self):
        self.edges = []  # a list of type  Edge
        # self.nodes = []  # a list of type  Node
        self.node_edge_list = []  # a list of type  EdgeList

    def get_nodes(self):
        nodes = []
        for edge_list in self.node_edge_list:
            nodes.append(edge_list.node.data)
        return nodes

    def create_node(self, data):
        # check if node exist
        filtered_nodes = list(filter(lambda n: n == data, self.get_nodes()))
        if len(filtered_nodes) > 0:
            # if node was found, return it
            return filtered_nodes[0]

        # if node not exist, create a new one
        index = len(self.node_edge_list)
        node = Node(index, data)
        edge_list = EdgeList(node)
        self.node_edge_list.append(edge_list)
        return node

    def add_edge(self, node_from, node_to):
        formatted_edges = self.get_formatted_edges()
        connection1 = "{} : {}".format(node_from.data, node_to.data)
        connection2 = "{} : {}".format(node_to.data, node_from.data)
        filtered_edges = list(filter(lambda e: (e == connection1 or e == connection2), formatted_edges))

        if len(filtered_edges) == 0:
            # If edge not exist, then create it
            edge = Edge(node_a=node_from, node_b=node_to)
            node_edges = self.node_edge_list[node_from.index]
            if not node_edges.edges:
                node_edges.edges = [edge]
            else:
                node_edges.add_edge(edge)

    def get_formatted_edges(self):
        formatted_list = []
        for edge_list in self.node_edge_list:
            edges = edge_list.edges
            if not edges:
                continue

            for edge in edges:
                connection = "{} : {}".format(edge.node_a.data, edge.node_b.data)
                formatted_list.append(connection)

        return formatted_list


if __name__ == '__main__':
    print("testing ListGraph...")
    dev_network = ListGraph()
    node1 = dev_network.create_node("virgi@gmail.com")
    node2 = dev_network.create_node("mirna@gmail.com")
    node3 = dev_network.create_node("luis@gmail.com")
    node4 = dev_network.create_node("eche@gmail.com")
    node5 = dev_network.create_node("cerv@gmail.com")

    print("nodes count = ", dev_network.get_nodes())

    dev_network.add_edge(node1, node2)
    dev_network.add_edge(node1, node3)
    dev_network.add_edge(node1, node4)
    dev_network.add_edge(node1, node5)
    dev_network.add_edge(node3, node4)

    dev_network.add_edge(node1, node2)
    dev_network.add_edge(node2, node1)

    edges = dev_network.get_formatted_edges()
    print("\n".join(edges))
