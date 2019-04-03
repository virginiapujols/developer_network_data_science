import DeveloperNetwork
import GitManager
import networkx as nx
import matplotlib.pyplot as plt

PROJECT_PATH = '/Users/virginiapujols/Documents/RIT/SEMESTER 4/Data science/project 3/che'

# 1. Connect to the git REPO and get the repo object with all commits, authors and files.
repo = GitManager.get_repo_local(PROJECT_PATH)


def get_dev_network_from_file():
    dev_network_list = []
    with open('dev_network.txt', 'r') as file:
        dev_network_list = file.read().splitlines()
    return dev_network_list


def create_dev_network():
    """ Part 1 Deliverables: A text file where each line represent an edge in the graph
    in the format "email1:email2" indicating an edge from email1 to email2 """

    # 2. Create a dictionary where
    #    Key   = file path committed
    #    Value = Author that touched that file during a commit
    files_to_developer = DeveloperNetwork.get_files_per_developer(repo)
    print('{} files saved!'.format(len(files_to_developer.keys())))

    # 3. Create a set object to save strings with the format: "email1:email2"

    dev_network_set = set()
    for file_path in files_to_developer:
        developer_emails = list(files_to_developer[file_path])

        for outer_dev_email in developer_emails:
            for inner_dev_email in developer_emails:
                if outer_dev_email == inner_dev_email:
                    continue

                dev_to_dev_connection = DeveloperNetwork.create_nodes_connection(outer_dev_email,
                                                                                 inner_dev_email,
                                                                                 dev_network_set)
                if dev_to_dev_connection is None:
                    continue
                dev_network_set.add(dev_to_dev_connection)

    # 4. Save the networks into a txt file
    with open('dev_network.txt', 'w+') as file:
        file.write('\n'.join(list(dev_network_set)))

    print('DONE!!')
    print('{} developer combinations'.format(len(list(dev_network_set))))
    return list(dev_network_set)


def create_graph(node_list, edges_list):
    G = nx.Graph()

    # create nodes from committer email
    G.add_nodes_from(node_list)

    # create edges from dev_network with format "email1:email2"
    # for connection in edges_list:
    #     dev_email1 = connection.split(' : ')[0]
    #     dev_email2 = connection.split(' : ')[1]
    #     G.add_edge(dev_email1, dev_email2)
    G.add_edges_from(edges_list)

    print('Nodes created: ', G.number_of_nodes())
    print('Edges created: ', G.number_of_edges())
    return G


def draw_graph(p_graph):
    nx.draw(p_graph, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    # PROGRAM EXECUTION
    committer_emails = GitManager.get_committer_list(repo)

    # developer_connections = create_dev_network()
    orig_developer_connections = get_dev_network_from_file()

    # Convert committer email to number index, for better understanding of the graph result.
    committer_email_index_dict = dict()
    count = 0
    for email in committer_emails:
        count += 1
        committer_email_index_dict[email] = count

    new_developer_connections = []
    for connection in orig_developer_connections:
        dev_email1 = connection.split(' : ')[0]
        dev_email2 = connection.split(' : ')[1]

        # new_connection = "{} : {}".format(committer_email_index_dict[dev_email1], committer_email_index_dict[dev_email2])
        new_connection = (committer_email_index_dict[dev_email1], committer_email_index_dict[dev_email2])
        new_developer_connections.append(new_connection)

    dev_graph = create_graph(committer_email_index_dict.values(), new_developer_connections)
    draw_graph(dev_graph)

    # test
    # test_graph = nx.Graph()
    # for i in range(1,6):
    #     test_graph.add_node(i)
    #
    # test_graph.add_edges_from([(1, 2),
    #                       (5, 4),
    #                       (3, 1),
    #                       (2, 4),
    #                       (3, 2),
    #                       ])
    # draw_graph(test_graph)


